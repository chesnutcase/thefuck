import re
from thefuck.utils import replace_argument, for_app


@for_app('composer')
def match(command):
    # determine error type
    # matching "did you mean this" is not enough as composer also gives spelling suggestions for mistakes other than mispelled commands
    is_undefined_command_error = r"[Symfony\Component\Console\Exception\CommandNotFoundException]" in command.output
    suggestions_present = (('did you mean this?' in command.output.lower()
                            or 'did you mean one of these?' in command.output.lower()))
    return is_undefined_command_error and suggestions_present


def get_new_command(command):
    # since the command class already tells us the original argument, we need not resort to regex
    broken_cmd = command.script_parts[1]
    one_suggestion_only = 'did you mean this?' in command.output.lower()
    if one_suggestion_only:
        new_cmd = re.findall(r'Did you mean this\?[^\n]*\n\s*([^\n]*)', command.output)
        return replace_argument(command.script, broken_cmd, new_cmd[0].strip())
    else:
        # there are multiple suggestions
        # trim output text to make it more digestable by regex
        trim_start_index = command.output.find("Did you mean one of these?")
        short_output = command.output[trim_start_index:]
        stripped_lines = [line.strip() for line in short_output.split("\n")]
        # each of the suggested commands can be found from index 1 to the first occurence of blank string
        try:
            end_index = stripped_lines.index('')
        except ValueError:
            end_index = None
        suggested_commands = stripped_lines[1:end_index]
        return [
            replace_argument(command.script, broken_cmd, cmd.strip())
            for cmd in suggested_commands
        ]
