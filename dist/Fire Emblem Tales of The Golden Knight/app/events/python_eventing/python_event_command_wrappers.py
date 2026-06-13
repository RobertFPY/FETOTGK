
###############################################################################################################################
# This code was generated using `source_generator.py`. DO NOT MAKE ANY EDITS TO THIS FILE - YOUR CHANGES WILL BE OVERWRITTEN. #
###############################################################################################################################
from typing import Any, Callable, List, Tuple
from .. import event_commands, event_validators

def optional_value_filter(required_keywords: List[str]) -> Callable[[Tuple[str, Any]], bool]:
    # pair is a (key, value) pair
    return lambda pair: (pair[0] in required_keywords) or (pair[1] is not None)
def music(Music: Any, FadeIn: Any = None, ) -> event_commands.Music:
    command_t = event_commands.Music
    parameters: dict[str, Any] = {"Music": Music, "FadeIn": FadeIn}
    parameters = dict(filter(optional_value_filter(["Music"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def music_fade_back(FadeOut: Any = None, ) -> event_commands.MusicFadeBack:
    command_t = event_commands.MusicFadeBack
    parameters: dict[str, Any] = {"FadeOut": FadeOut}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def music_clear(FadeOut: Any = None, ) -> event_commands.MusicClear:
    command_t = event_commands.MusicClear
    parameters: dict[str, Any] = {"FadeOut": FadeOut}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def sound(Sound: Any, Volume: Any = None, ) -> event_commands.Sound:
    command_t = event_commands.Sound
    parameters: dict[str, Any] = {"Sound": Sound, "Volume": Volume}
    parameters = dict(filter(optional_value_filter(["Sound"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def stop_sound(Sound: Any, ) -> event_commands.StopSound:
    command_t = event_commands.StopSound
    parameters: dict[str, Any] = {"Sound": Sound}
    parameters = dict(filter(optional_value_filter(["Sound"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_music(Phase: Any, Music: Any, ) -> event_commands.ChangeMusic:
    command_t = event_commands.ChangeMusic
    parameters: dict[str, Any] = {"Phase": Phase, "Music": Music}
    parameters = dict(filter(optional_value_filter(["Phase", "Music"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_special_music(SpecialMusicType: Any, Music: Any, ) -> event_commands.ChangeSpecialMusic:
    command_t = event_commands.ChangeSpecialMusic
    parameters: dict[str, Any] = {"SpecialMusicType": SpecialMusicType, "Music": Music}
    parameters = dict(filter(optional_value_filter(["SpecialMusicType", "Music"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_portrait(Portrait: Any, ScreenPosition: Any, Slide: Any = None, ExpressionList: Any = None, SpeedMult: Any = None, ) -> event_commands.AddPortrait:
    command_t = event_commands.AddPortrait
    parameters: dict[str, Any] = {"Portrait": Portrait, "ScreenPosition": ScreenPosition, "Slide": Slide, "ExpressionList": ExpressionList, "SpeedMult": SpeedMult}
    parameters = dict(filter(optional_value_filter(["Portrait", "ScreenPosition"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def multi_add_portrait(Portrait1: Any, ScreenPosition1: Any, Portrait2: Any, ScreenPosition2: Any, Portrait3: Any = None, ScreenPosition3: Any = None, Portrait4: Any = None, ScreenPosition4: Any = None, ) -> event_commands.MultiAddPortrait:
    command_t = event_commands.MultiAddPortrait
    parameters: dict[str, Any] = {"Portrait1": Portrait1, "ScreenPosition1": ScreenPosition1, "Portrait2": Portrait2, "ScreenPosition2": ScreenPosition2, "Portrait3": Portrait3, "ScreenPosition3": ScreenPosition3, "Portrait4": Portrait4, "ScreenPosition4": ScreenPosition4}
    parameters = dict(filter(optional_value_filter(["Portrait1", "ScreenPosition1", "Portrait2", "ScreenPosition2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_portrait(Portrait: Any, SpeedMult: Any = None, Slide: Any = None, ) -> event_commands.RemovePortrait:
    command_t = event_commands.RemovePortrait
    parameters: dict[str, Any] = {"Portrait": Portrait, "SpeedMult": SpeedMult, "Slide": Slide}
    parameters = dict(filter(optional_value_filter(["Portrait"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def multi_remove_portrait(Portrait1: Any, Portrait2: Any, Portrait3: Any = None, Portrait4: Any = None, ) -> event_commands.MultiRemovePortrait:
    command_t = event_commands.MultiRemovePortrait
    parameters: dict[str, Any] = {"Portrait1": Portrait1, "Portrait2": Portrait2, "Portrait3": Portrait3, "Portrait4": Portrait4}
    parameters = dict(filter(optional_value_filter(["Portrait1", "Portrait2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_all_portraits() -> event_commands.RemoveAllPortraits:
    command_t = event_commands.RemoveAllPortraits
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def move_portrait(Portrait: Any, ScreenPosition: Any, SpeedMult: Any = None, ) -> event_commands.MovePortrait:
    command_t = event_commands.MovePortrait
    parameters: dict[str, Any] = {"Portrait": Portrait, "ScreenPosition": ScreenPosition, "SpeedMult": SpeedMult}
    parameters = dict(filter(optional_value_filter(["Portrait", "ScreenPosition"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def bop_portrait(Portrait: Any, NumBops: Any = None, Time: Any = None, ) -> event_commands.BopPortrait:
    command_t = event_commands.BopPortrait
    parameters: dict[str, Any] = {"Portrait": Portrait, "NumBops": NumBops, "Time": Time}
    parameters = dict(filter(optional_value_filter(["Portrait"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def mirror_portrait(Portrait: Any, SpeedMult: Any = None, ) -> event_commands.MirrorPortrait:
    command_t = event_commands.MirrorPortrait
    parameters: dict[str, Any] = {"Portrait": Portrait, "SpeedMult": SpeedMult}
    parameters = dict(filter(optional_value_filter(["Portrait"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def expression(Portrait: Any, ExpressionList: Any, ) -> event_commands.Expression:
    command_t = event_commands.Expression
    parameters: dict[str, Any] = {"Portrait": Portrait, "ExpressionList": ExpressionList}
    parameters = dict(filter(optional_value_filter(["Portrait", "ExpressionList"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def speak_style(Style: Any, Speaker: Any = None, Position: Any = None, Width: Any = None, Speed: Any = None, FontColor: Any = None, FontType: Any = None, Background: Any = None, NumLines: Any = None, DrawCursor: Any = None, MessageTail: Any = None, Transparency: Any = None, NameTagBg: Any = None, BoopSound: Any = None, ) -> event_commands.SpeakStyle:
    command_t = event_commands.SpeakStyle
    parameters: dict[str, Any] = {"Style": Style, "Speaker": Speaker, "Position": Position, "Width": Width, "Speed": Speed, "FontColor": FontColor, "FontType": FontType, "Background": Background, "NumLines": NumLines, "DrawCursor": DrawCursor, "MessageTail": MessageTail, "Transparency": Transparency, "NameTagBg": NameTagBg, "BoopSound": BoopSound}
    parameters = dict(filter(optional_value_filter(["Style"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def speak(SpeakerOrStyle: Any, Text: Any, TextPosition: Any = None, Width: Any = None, StyleNid: Any = None, TextSpeed: Any = None, FontColor: Any = None, FontType: Any = None, DialogBox: Any = None, NumLines: Any = None, DrawCursor: Any = None, MessageTail: Any = None, Transparency: Any = None, NameTagBg: Any = None, BoopSound: Any = None, ) -> event_commands.Speak:
    command_t = event_commands.Speak
    parameters: dict[str, Any] = {"SpeakerOrStyle": SpeakerOrStyle, "Text": Text, "TextPosition": TextPosition, "Width": Width, "StyleNid": StyleNid, "TextSpeed": TextSpeed, "FontColor": FontColor, "FontType": FontType, "DialogBox": DialogBox, "NumLines": NumLines, "DrawCursor": DrawCursor, "MessageTail": MessageTail, "Transparency": Transparency, "NameTagBg": NameTagBg, "BoopSound": BoopSound}
    parameters = dict(filter(optional_value_filter(["SpeakerOrStyle", "Text"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def say(SpeakerOrStyle: Any, *Text: Any, TextPosition: Any = None, Width: Any = None, StyleNid: Any = None, TextSpeed: Any = None, FontColor: Any = None, FontType: Any = None, DialogBox: Any = None, NumLines: Any = None, DrawCursor: Any = None, MessageTail: Any = None, Transparency: Any = None, NameTagBg: Any = None, BoopSound: Any = None, ) -> event_commands.Say:
    command_t = event_commands.Say
    parameters: dict[str, Any] = {"SpeakerOrStyle": SpeakerOrStyle, "Text": Text, "TextPosition": TextPosition, "Width": Width, "StyleNid": StyleNid, "TextSpeed": TextSpeed, "FontColor": FontColor, "FontType": FontType, "DialogBox": DialogBox, "NumLines": NumLines, "DrawCursor": DrawCursor, "MessageTail": MessageTail, "Transparency": Transparency, "NameTagBg": NameTagBg, "BoopSound": BoopSound}
    parameters = dict(filter(optional_value_filter(["SpeakerOrStyle", "*Text"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unhold(Nid: Any, ) -> event_commands.Unhold:
    command_t = event_commands.Unhold
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unpause(Nid: Any = None, ) -> event_commands.Unpause:
    command_t = event_commands.Unpause
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def transition(Direction: Any = None, Speed: Any = None, Color3: Any = None, Panorama: Any = None, ) -> event_commands.Transition:
    command_t = event_commands.Transition
    parameters: dict[str, Any] = {"Direction": Direction, "Speed": Speed, "Color3": Color3, "Panorama": Panorama}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_background(Panorama: Any = None, Speed: Any = None, ) -> event_commands.ChangeBackground:
    command_t = event_commands.ChangeBackground
    parameters: dict[str, Any] = {"Panorama": Panorama, "Speed": Speed}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def pause_background(PauseAt: Any = None, ) -> event_commands.PauseBackground:
    command_t = event_commands.PauseBackground
    parameters: dict[str, Any] = {"PauseAt": PauseAt}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unpause_background() -> event_commands.UnpauseBackground:
    command_t = event_commands.UnpauseBackground
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def disp_cursor(ShowCursor: Any, ) -> event_commands.DispCursor:
    command_t = event_commands.DispCursor
    parameters: dict[str, Any] = {"ShowCursor": ShowCursor}
    parameters = dict(filter(optional_value_filter(["ShowCursor"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def move_cursor(Position: Any, Speed: Any = None, ) -> event_commands.MoveCursor:
    command_t = event_commands.MoveCursor
    parameters: dict[str, Any] = {"Position": Position, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Position"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def center_cursor(Position: Any, Speed: Any = None, ) -> event_commands.CenterCursor:
    command_t = event_commands.CenterCursor
    parameters: dict[str, Any] = {"Position": Position, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Position"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def smooth_camera_path(Positions: Any, TotalSpeed: Any = None, TilesPerSecond: Any = None, Music: Any = None, ) -> event_commands.SmoothCameraPath:
    command_t = event_commands.SmoothCameraPath
    parameters: dict[str, Any] = {"Positions": Positions, "TotalSpeed": TotalSpeed, "TilesPerSecond": TilesPerSecond, "Music": Music}
    parameters = dict(filter(optional_value_filter(["Positions"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def flicker_cursor(Position: Any, ) -> event_commands.FlickerCursor:
    command_t = event_commands.FlickerCursor
    parameters: dict[str, Any] = {"Position": Position}
    parameters = dict(filter(optional_value_filter(["Position"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def screen_shake(Duration: Any, ShakeType: Any = None, ) -> event_commands.ScreenShake:
    command_t = event_commands.ScreenShake
    parameters: dict[str, Any] = {"Duration": Duration, "ShakeType": ShakeType}
    parameters = dict(filter(optional_value_filter(["Duration"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def screen_shake_end() -> event_commands.ScreenShakeEnd:
    command_t = event_commands.ScreenShakeEnd
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def game_var(Nid: Any, Expression: Any, ) -> event_commands.GameVar:
    command_t = event_commands.GameVar
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def inc_game_var(Nid: Any, Expression: Any = None, ) -> event_commands.IncGameVar:
    command_t = event_commands.IncGameVar
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def level_var(Nid: Any, Expression: Any, ) -> event_commands.LevelVar:
    command_t = event_commands.LevelVar
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def inc_level_var(Nid: Any, Expression: Any = None, ) -> event_commands.IncLevelVar:
    command_t = event_commands.IncLevelVar
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_next_chapter(Chapter: Any, ) -> event_commands.SetNextChapter:
    command_t = event_commands.SetNextChapter
    parameters: dict[str, Any] = {"Chapter": Chapter}
    parameters = dict(filter(optional_value_filter(["Chapter"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def enable_convoy(Activated: Any, ) -> event_commands.EnableConvoy:
    command_t = event_commands.EnableConvoy
    parameters: dict[str, Any] = {"Activated": Activated}
    parameters = dict(filter(optional_value_filter(["Activated"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def enable_repair_shop(Activated: Any, ) -> event_commands.EnableRepairShop:
    command_t = event_commands.EnableRepairShop
    parameters: dict[str, Any] = {"Activated": Activated}
    parameters = dict(filter(optional_value_filter(["Activated"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def enable_supports(Activated: Any, ) -> event_commands.EnableSupports:
    command_t = event_commands.EnableSupports
    parameters: dict[str, Any] = {"Activated": Activated}
    parameters = dict(filter(optional_value_filter(["Activated"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def enable_turnwheel(Activated: Any, ) -> event_commands.EnableTurnwheel:
    command_t = event_commands.EnableTurnwheel
    parameters: dict[str, Any] = {"Activated": Activated}
    parameters = dict(filter(optional_value_filter(["Activated"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def enable_fog_of_war(Activated: Any, ) -> event_commands.EnableFogOfWar:
    command_t = event_commands.EnableFogOfWar
    parameters: dict[str, Any] = {"Activated": Activated}
    parameters = dict(filter(optional_value_filter(["Activated"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_fog_of_war(FogOfWarType: Any, Radius: Any, AIRadius: Any = None, OtherRadius: Any = None, FogOfWarColor: Any = None, ) -> event_commands.SetFogOfWar:
    command_t = event_commands.SetFogOfWar
    parameters: dict[str, Any] = {"FogOfWarType": FogOfWarType, "Radius": Radius, "AIRadius": AIRadius, "OtherRadius": OtherRadius, "FogOfWarColor": FogOfWarColor}
    parameters = dict(filter(optional_value_filter(["FogOfWarType", "Radius"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def end_turn(Team: Any = None, ) -> event_commands.EndTurn:
    command_t = event_commands.EndTurn
    parameters: dict[str, Any] = {"Team": Team}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def win_game() -> event_commands.WinGame:
    command_t = event_commands.WinGame
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def lose_game() -> event_commands.LoseGame:
    command_t = event_commands.LoseGame
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def main_menu() -> event_commands.MainMenu:
    command_t = event_commands.MainMenu
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def force_chapter_clean_up() -> event_commands.ForceChapterCleanUp:
    command_t = event_commands.ForceChapterCleanUp
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def skip_save(TrueOrFalse: Any, ) -> event_commands.SkipSave:
    command_t = event_commands.SkipSave
    parameters: dict[str, Any] = {"TrueOrFalse": TrueOrFalse}
    parameters = dict(filter(optional_value_filter(["TrueOrFalse"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def activate_turnwheel(Force: Any = None, ) -> event_commands.ActivateTurnwheel:
    command_t = event_commands.ActivateTurnwheel
    parameters: dict[str, Any] = {"Force": Force}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def battle_save(SaveName: Any = None, ) -> event_commands.BattleSave:
    command_t = event_commands.BattleSave
    parameters: dict[str, Any] = {"SaveName": SaveName}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def delete_save(SaveSlot: Any = None, ) -> event_commands.DeleteSave:
    command_t = event_commands.DeleteSave
    parameters: dict[str, Any] = {"SaveSlot": SaveSlot}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def clear_turnwheel() -> event_commands.ClearTurnwheel:
    command_t = event_commands.ClearTurnwheel
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def stop_turnwheel_recording() -> event_commands.StopTurnwheelRecording:
    command_t = event_commands.StopTurnwheelRecording
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def start_turnwheel_recording() -> event_commands.StartTurnwheelRecording:
    command_t = event_commands.StartTurnwheelRecording
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_tilemap(Tilemap: Any, PositionOffset: Any = None, LoadTilemap: Any = None, ) -> event_commands.ChangeTilemap:
    command_t = event_commands.ChangeTilemap
    parameters: dict[str, Any] = {"Tilemap": Tilemap, "PositionOffset": PositionOffset, "LoadTilemap": LoadTilemap}
    parameters = dict(filter(optional_value_filter(["Tilemap"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_bg_tilemap(Tilemap: Any = None, ) -> event_commands.ChangeBgTilemap:
    command_t = event_commands.ChangeBgTilemap
    parameters: dict[str, Any] = {"Tilemap": Tilemap}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_game_board_bounds(MinX: Any, MinY: Any, MaxX: Any, MaxY: Any, ) -> event_commands.SetGameBoardBounds:
    command_t = event_commands.SetGameBoardBounds
    parameters: dict[str, Any] = {"MinX": MinX, "MinY": MinY, "MaxX": MaxX, "MaxY": MaxY}
    parameters = dict(filter(optional_value_filter(["MinX", "MinY", "MaxX", "MaxY"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_game_board_bounds() -> event_commands.RemoveGameBoardBounds:
    command_t = event_commands.RemoveGameBoardBounds
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def load_unit(UniqueUnit: Any, Team: Any = None, AI: Any = None, ) -> event_commands.LoadUnit:
    command_t = event_commands.LoadUnit
    parameters: dict[str, Any] = {"UniqueUnit": UniqueUnit, "Team": Team, "AI": AI}
    parameters = dict(filter(optional_value_filter(["UniqueUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def make_generic(Nid: Any, Klass: Any, Level: Any, Team: Any, AI: Any = None, Faction: Any = None, AnimationVariant: Any = None, ItemList: Any = None, ) -> event_commands.MakeGeneric:
    command_t = event_commands.MakeGeneric
    parameters: dict[str, Any] = {"Nid": Nid, "Klass": Klass, "Level": Level, "Team": Team, "AI": AI, "Faction": Faction, "AnimationVariant": AnimationVariant, "ItemList": ItemList}
    parameters = dict(filter(optional_value_filter(["Nid", "Klass", "Level", "Team"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def create_unit(Unit: Any, Nid: Any = None, Level: Any = None, Position: Any = None, EntryType: Any = None, Placement: Any = None, ) -> event_commands.CreateUnit:
    command_t = event_commands.CreateUnit
    parameters: dict[str, Any] = {"Unit": Unit, "Nid": Nid, "Level": Level, "Position": Position, "EntryType": EntryType, "Placement": Placement}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def copy_stat(Unit: Any, Unit2: Any, ) -> event_commands.CopyStat:
    command_t = event_commands.CopyStat
    parameters: dict[str, Any] = {"Unit": Unit, "Unit2": Unit2}
    parameters = dict(filter(optional_value_filter(["Unit", "Unit2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_unit(Unit: Any, Position: Any = None, EntryType: Any = None, Placement: Any = None, AnimationType: Any = None, ) -> event_commands.AddUnit:
    command_t = event_commands.AddUnit
    parameters: dict[str, Any] = {"Unit": Unit, "Position": Position, "EntryType": EntryType, "Placement": Placement, "AnimationType": AnimationType}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def move_unit(Unit: Any, Position: Any = None, MovementType: Any = None, Placement: Any = None, Speed: Any = None, ) -> event_commands.MoveUnit:
    command_t = event_commands.MoveUnit
    parameters: dict[str, Any] = {"Unit": Unit, "Position": Position, "MovementType": MovementType, "Placement": Placement, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_unit(Unit: Any, RemoveType: Any = None, AnimationType: Any = None, ) -> event_commands.RemoveUnit:
    command_t = event_commands.RemoveUnit
    parameters: dict[str, Any] = {"Unit": Unit, "RemoveType": RemoveType, "AnimationType": AnimationType}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def kill_unit(Unit: Any, ) -> event_commands.KillUnit:
    command_t = event_commands.KillUnit
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_all_units() -> event_commands.RemoveAllUnits:
    command_t = event_commands.RemoveAllUnits
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_all_enemies() -> event_commands.RemoveAllEnemies:
    command_t = event_commands.RemoveAllEnemies
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def interact_unit(Unit: Any, Position: Any, CombatScript: Any = None, Ability: Any = None, Rounds: Any = None, ) -> event_commands.InteractUnit:
    command_t = event_commands.InteractUnit
    parameters: dict[str, Any] = {"Unit": Unit, "Position": Position, "CombatScript": CombatScript, "Ability": Ability, "Rounds": Rounds}
    parameters = dict(filter(optional_value_filter(["Unit", "Position"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_combat_script(CombatScript: Any, ) -> event_commands.SetCombatScript:
    command_t = event_commands.SetCombatScript
    parameters: dict[str, Any] = {"CombatScript": CombatScript}
    parameters = dict(filter(optional_value_filter(["CombatScript"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def pose_unit(Unit: Any, Pose: Any, Direction: Any = None, ) -> event_commands.PoseUnit:
    command_t = event_commands.PoseUnit
    parameters: dict[str, Any] = {"Unit": Unit, "Pose": Pose, "Direction": Direction}
    parameters = dict(filter(optional_value_filter(["Unit", "Pose"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_name(Unit: Any, String: Any, ) -> event_commands.SetName:
    command_t = event_commands.SetName
    parameters: dict[str, Any] = {"Unit": Unit, "String": String}
    parameters = dict(filter(optional_value_filter(["Unit", "String"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_variant(Unit: Any, String: Any = None, ) -> event_commands.SetVariant:
    command_t = event_commands.SetVariant
    parameters: dict[str, Any] = {"Unit": Unit, "String": String}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_current_hp(Unit: Any, HP: Any, ) -> event_commands.SetCurrentHP:
    command_t = event_commands.SetCurrentHP
    parameters: dict[str, Any] = {"Unit": Unit, "HP": HP}
    parameters = dict(filter(optional_value_filter(["Unit", "HP"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_current_mana(Unit: Any, Mana: Any, ) -> event_commands.SetCurrentMana:
    command_t = event_commands.SetCurrentMana
    parameters: dict[str, Any] = {"Unit": Unit, "Mana": Mana}
    parameters = dict(filter(optional_value_filter(["Unit", "Mana"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_fatigue(Unit: Any, Fatigue: Any, ) -> event_commands.AddFatigue:
    command_t = event_commands.AddFatigue
    parameters: dict[str, Any] = {"Unit": Unit, "Fatigue": Fatigue}
    parameters = dict(filter(optional_value_filter(["Unit", "Fatigue"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_unit_field(GlobalUnit: Any, Key: Any, Value: Any, ) -> event_commands.SetUnitField:
    command_t = event_commands.SetUnitField
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Key": Key, "Value": Value}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Key", "Value"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_unit_note(Unit: Any, Key: Any, Value: Any, ) -> event_commands.SetUnitNote:
    command_t = event_commands.SetUnitNote
    parameters: dict[str, Any] = {"Unit": Unit, "Key": Key, "Value": Value}
    parameters = dict(filter(optional_value_filter(["Unit", "Key", "Value"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_unit_note(Unit: Any, Key: Any, ) -> event_commands.RemoveUnitNote:
    command_t = event_commands.RemoveUnitNote
    parameters: dict[str, Any] = {"Unit": Unit, "Key": Key}
    parameters = dict(filter(optional_value_filter(["Unit", "Key"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def resurrect(GlobalUnit: Any, ) -> event_commands.Resurrect:
    command_t = event_commands.Resurrect
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit}
    parameters = dict(filter(optional_value_filter(["GlobalUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def reset(Unit: Any, ) -> event_commands.Reset:
    command_t = event_commands.Reset
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def has_attacked(Unit: Any, ) -> event_commands.HasAttacked:
    command_t = event_commands.HasAttacked
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def has_traded(Unit: Any, ) -> event_commands.HasTraded:
    command_t = event_commands.HasTraded
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def has_visited(Unit: Any, ) -> event_commands.HasVisited:
    command_t = event_commands.HasVisited
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def has_finished(Unit: Any, ) -> event_commands.HasFinished:
    command_t = event_commands.HasFinished
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def recruit_generic(Unit: Any, Nid: Any, Name: Any = None, ) -> event_commands.RecruitGeneric:
    command_t = event_commands.RecruitGeneric
    parameters: dict[str, Any] = {"Unit": Unit, "Nid": Nid, "Name": Name}
    parameters = dict(filter(optional_value_filter(["Unit", "Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_group(Group: Any, StartingGroup: Any = None, EntryType: Any = None, Placement: Any = None, ) -> event_commands.AddGroup:
    command_t = event_commands.AddGroup
    parameters: dict[str, Any] = {"Group": Group, "StartingGroup": StartingGroup, "EntryType": EntryType, "Placement": Placement}
    parameters = dict(filter(optional_value_filter(["Group"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def spawn_group(Group: Any, CardinalDirection: Any, StartingGroup: Any, MovementType: Any = None, Placement: Any = None, ) -> event_commands.SpawnGroup:
    command_t = event_commands.SpawnGroup
    parameters: dict[str, Any] = {"Group": Group, "CardinalDirection": CardinalDirection, "StartingGroup": StartingGroup, "MovementType": MovementType, "Placement": Placement}
    parameters = dict(filter(optional_value_filter(["Group", "CardinalDirection", "StartingGroup"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def move_group(Group: Any, StartingGroup: Any, MovementType: Any = None, Placement: Any = None, ) -> event_commands.MoveGroup:
    command_t = event_commands.MoveGroup
    parameters: dict[str, Any] = {"Group": Group, "StartingGroup": StartingGroup, "MovementType": MovementType, "Placement": Placement}
    parameters = dict(filter(optional_value_filter(["Group", "StartingGroup"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_group(Group: Any, RemoveType: Any = None, ) -> event_commands.RemoveGroup:
    command_t = event_commands.RemoveGroup
    parameters: dict[str, Any] = {"Group": Group, "RemoveType": RemoveType}
    parameters = dict(filter(optional_value_filter(["Group"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def give_item(GlobalUnitOrConvoy: Any, Item: Any, Party: Any = None, ) -> event_commands.GiveItem:
    command_t = event_commands.GiveItem
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item, "Party": Party}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def equip_item(GlobalUnit: Any, Item: Any, ) -> event_commands.EquipItem:
    command_t = event_commands.EquipItem
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Item": Item}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Item"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def sort_inventory(GlobalUnit: Any, ) -> event_commands.SortInventory:
    command_t = event_commands.SortInventory
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit}
    parameters = dict(filter(optional_value_filter(["GlobalUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_item(GlobalUnitOrConvoy: Any, Item: Any, Party: Any = None, ) -> event_commands.RemoveItem:
    command_t = event_commands.RemoveItem
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item, "Party": Party}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def move_item(Giver: Any, Receiver: Any, Item: Any = None, ) -> event_commands.MoveItem:
    command_t = event_commands.MoveItem
    parameters: dict[str, Any] = {"Giver": Giver, "Receiver": Receiver, "Item": Item}
    parameters = dict(filter(optional_value_filter(["Giver", "Receiver"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def move_item_between_convoys(Item: Any, Party1: Any, Party2: Any, ) -> event_commands.MoveItemBetweenConvoys:
    command_t = event_commands.MoveItemBetweenConvoys
    parameters: dict[str, Any] = {"Item": Item, "Party1": Party1, "Party2": Party2}
    parameters = dict(filter(optional_value_filter(["Item", "Party1", "Party2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def open_convoy(GlobalUnit: Any, ) -> event_commands.OpenConvoy:
    command_t = event_commands.OpenConvoy
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit}
    parameters = dict(filter(optional_value_filter(["GlobalUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_item_uses(GlobalUnitOrConvoy: Any, Item: Any, Uses: Any, ) -> event_commands.SetItemUses:
    command_t = event_commands.SetItemUses
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item, "Uses": Uses}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item", "Uses"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_item_data(GlobalUnitOrConvoy: Any, Item: Any, Nid: Any, Expression: Any, ) -> event_commands.SetItemData:
    command_t = event_commands.SetItemData
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item, "Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item", "Nid", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_item_droppable(GlobalUnit: Any, Item: Any, Droppable: Any, ) -> event_commands.SetItemDroppable:
    command_t = event_commands.SetItemDroppable
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Item": Item, "Droppable": Droppable}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Item", "Droppable"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def break_item(GlobalUnitOrConvoy: Any, Item: Any, ) -> event_commands.BreakItem:
    command_t = event_commands.BreakItem
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_item_name(GlobalUnitOrConvoy: Any, Item: Any, String: Any, ) -> event_commands.ChangeItemName:
    command_t = event_commands.ChangeItemName
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item, "String": String}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item", "String"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_item_desc(GlobalUnitOrConvoy: Any, Item: Any, String: Any, ) -> event_commands.ChangeItemDesc:
    command_t = event_commands.ChangeItemDesc
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item, "String": String}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item", "String"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_item_to_multiitem(GlobalUnitOrConvoy: Any, MultiItem: Any, ChildItem: Any, ) -> event_commands.AddItemToMultiitem:
    command_t = event_commands.AddItemToMultiitem
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "MultiItem": MultiItem, "ChildItem": ChildItem}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "MultiItem", "ChildItem"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_item_from_multiitem(GlobalUnitOrConvoy: Any, MultiItem: Any, ChildItem: Any = None, ) -> event_commands.RemoveItemFromMultiitem:
    command_t = event_commands.RemoveItemFromMultiitem
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "MultiItem": MultiItem, "ChildItem": ChildItem}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "MultiItem"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_item_component(GlobalUnitOrConvoy: Any, Item: Any, ItemComponent: Any, Expression: Any = None, ) -> event_commands.AddItemComponent:
    command_t = event_commands.AddItemComponent
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item, "ItemComponent": ItemComponent, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item", "ItemComponent"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def modify_item_component(GlobalUnitOrConvoy: Any, Item: Any, ItemComponent: Any, Expression: Any, ComponentProperty: Any = None, ) -> event_commands.ModifyItemComponent:
    command_t = event_commands.ModifyItemComponent
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item, "ItemComponent": ItemComponent, "Expression": Expression, "ComponentProperty": ComponentProperty}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item", "ItemComponent", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_item_component(GlobalUnitOrConvoy: Any, Item: Any, ItemComponent: Any, ) -> event_commands.RemoveItemComponent:
    command_t = event_commands.RemoveItemComponent
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item, "ItemComponent": ItemComponent}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item", "ItemComponent"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_skill_component(GlobalUnit: Any, Skill: Any, SkillComponent: Any, Expression: Any = None, ) -> event_commands.AddSkillComponent:
    command_t = event_commands.AddSkillComponent
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Skill": Skill, "SkillComponent": SkillComponent, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Skill", "SkillComponent"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def modify_skill_component(GlobalUnit: Any, Skill: Any, SkillComponent: Any, Expression: Any, ComponentProperty: Any = None, ) -> event_commands.ModifySkillComponent:
    command_t = event_commands.ModifySkillComponent
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Skill": Skill, "SkillComponent": SkillComponent, "Expression": Expression, "ComponentProperty": ComponentProperty}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Skill", "SkillComponent", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_skill_component(GlobalUnit: Any, Skill: Any, SkillComponent: Any, ) -> event_commands.RemoveSkillComponent:
    command_t = event_commands.RemoveSkillComponent
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Skill": Skill, "SkillComponent": SkillComponent}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Skill", "SkillComponent"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def give_money(Money: Any, Party: Any = None, ) -> event_commands.GiveMoney:
    command_t = event_commands.GiveMoney
    parameters: dict[str, Any] = {"Money": Money, "Party": Party}
    parameters = dict(filter(optional_value_filter(["Money"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def give_bexp(Bexp: Any, Party: Any = None, String: Any = None, ) -> event_commands.GiveBexp:
    command_t = event_commands.GiveBexp
    parameters: dict[str, Any] = {"Bexp": Bexp, "Party": Party, "String": String}
    parameters = dict(filter(optional_value_filter(["Bexp"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def give_exp(GlobalUnit: Any, Experience: Any, ) -> event_commands.GiveExp:
    command_t = event_commands.GiveExp
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Experience": Experience}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Experience"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_exp(GlobalUnit: Any, Experience: Any, ) -> event_commands.SetExp:
    command_t = event_commands.SetExp
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Experience": Experience}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Experience"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def give_wexp(GlobalUnit: Any, WeaponType: Any, Integer: Any, ) -> event_commands.GiveWexp:
    command_t = event_commands.GiveWexp
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "WeaponType": WeaponType, "Integer": Integer}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "WeaponType", "Integer"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_wexp(GlobalUnit: Any, WeaponType: Any, WholeNumber: Any, ) -> event_commands.SetWexp:
    command_t = event_commands.SetWexp
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "WeaponType": WeaponType, "WholeNumber": WholeNumber}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "WeaponType", "WholeNumber"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def give_skill(GlobalUnit: Any, Skill: Any, Initiator: Any = None, ) -> event_commands.GiveSkill:
    command_t = event_commands.GiveSkill
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Skill": Skill, "Initiator": Initiator}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Skill"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_skill(GlobalUnit: Any, Skill: Any, Count: Any = None, ) -> event_commands.RemoveSkill:
    command_t = event_commands.RemoveSkill
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Skill": Skill, "Count": Count}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Skill"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_skill_data(GlobalUnit: Any, Skill: Any, Nid: Any, Expression: Any, ) -> event_commands.SetSkillData:
    command_t = event_commands.SetSkillData
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Skill": Skill, "Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Skill", "Nid", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_ai(GlobalUnit: Any, AI: Any, ) -> event_commands.ChangeAI:
    command_t = event_commands.ChangeAI
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "AI": AI}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "AI"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_roam_ai(GlobalUnit: Any, AI: Any, ) -> event_commands.ChangeRoamAI:
    command_t = event_commands.ChangeRoamAI
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "AI": AI}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "AI"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_ai_group(GlobalUnit: Any, AIGroup: Any, ) -> event_commands.ChangeAIGroup:
    command_t = event_commands.ChangeAIGroup
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "AIGroup": AIGroup}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "AIGroup"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_party(GlobalUnit: Any, Party: Any, ) -> event_commands.ChangeParty:
    command_t = event_commands.ChangeParty
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Party": Party}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Party"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_faction(GlobalUnit: Any, Faction: Any, ) -> event_commands.ChangeFaction:
    command_t = event_commands.ChangeFaction
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Faction": Faction}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Faction"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_team(GlobalUnit: Any, Team: Any, ) -> event_commands.ChangeTeam:
    command_t = event_commands.ChangeTeam
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Team": Team}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Team"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_portrait(GlobalUnit: Any, PortraitNid: Any, ) -> event_commands.ChangePortrait:
    command_t = event_commands.ChangePortrait
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "PortraitNid": PortraitNid}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "PortraitNid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_unit_desc(GlobalUnit: Any, String: Any, ) -> event_commands.ChangeUnitDesc:
    command_t = event_commands.ChangeUnitDesc
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "String": String}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "String"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_affinity(GlobalUnit: Any, Affinity: Any, ) -> event_commands.ChangeAffinity:
    command_t = event_commands.ChangeAffinity
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Affinity": Affinity}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Affinity"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_stats(GlobalUnit: Any, StatList: Any, ) -> event_commands.ChangeStats:
    command_t = event_commands.ChangeStats
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "StatList": StatList}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "StatList"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_stats(GlobalUnit: Any, StatList: Any, ) -> event_commands.SetStats:
    command_t = event_commands.SetStats
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "StatList": StatList}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "StatList"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_growths(GlobalUnit: Any, StatList: Any, ) -> event_commands.ChangeGrowths:
    command_t = event_commands.ChangeGrowths
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "StatList": StatList}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "StatList"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_growths(GlobalUnit: Any, StatList: Any, ) -> event_commands.SetGrowths:
    command_t = event_commands.SetGrowths
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "StatList": StatList}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "StatList"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_stat_cap_modifiers(GlobalUnit: Any, StatList: Any, ) -> event_commands.ChangeStatCapModifiers:
    command_t = event_commands.ChangeStatCapModifiers
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "StatList": StatList}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "StatList"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_stat_cap_modifiers(GlobalUnit: Any, StatList: Any, ) -> event_commands.SetStatCapModifiers:
    command_t = event_commands.SetStatCapModifiers
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "StatList": StatList}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "StatList"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_unit_level(GlobalUnit: Any, Level: Any, ) -> event_commands.SetUnitLevel:
    command_t = event_commands.SetUnitLevel
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Level": Level}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Level"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def autolevel_to(GlobalUnit: Any, Level: Any, GrowthMethod: Any = None, ) -> event_commands.AutolevelTo:
    command_t = event_commands.AutolevelTo
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Level": Level, "GrowthMethod": GrowthMethod}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Level"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_mode_autolevels(Level: Any, ) -> event_commands.SetModeAutolevels:
    command_t = event_commands.SetModeAutolevels
    parameters: dict[str, Any] = {"Level": Level}
    parameters = dict(filter(optional_value_filter(["Level"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_mode_rng(rng: Any, ) -> event_commands.SetModeRNG:
    command_t = event_commands.SetModeRNG
    parameters: dict[str, Any] = {"rng": rng}
    parameters = dict(filter(optional_value_filter(["rng"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def promote(GlobalUnit: Any, KlassList: Any = None, ) -> event_commands.Promote:
    command_t = event_commands.Promote
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "KlassList": KlassList}
    parameters = dict(filter(optional_value_filter(["GlobalUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_class(GlobalUnit: Any, KlassList: Any = None, ) -> event_commands.ChangeClass:
    command_t = event_commands.ChangeClass
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "KlassList": KlassList}
    parameters = dict(filter(optional_value_filter(["GlobalUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_tag(GlobalUnit: Any, Tag: Any, ) -> event_commands.AddTag:
    command_t = event_commands.AddTag
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Tag": Tag}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Tag"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_tag(GlobalUnit: Any, Tag: Any, ) -> event_commands.RemoveTag:
    command_t = event_commands.RemoveTag
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Tag": Tag}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Tag"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_talk(Unit1: Any, Unit2: Any, ) -> event_commands.AddTalk:
    command_t = event_commands.AddTalk
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_talk(Unit1: Any, Unit2: Any, ) -> event_commands.RemoveTalk:
    command_t = event_commands.RemoveTalk
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def hide_talk(Unit1: Any, Unit2: Any, ) -> event_commands.HideTalk:
    command_t = event_commands.HideTalk
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unhide_talk(Unit1: Any, Unit2: Any, ) -> event_commands.UnhideTalk:
    command_t = event_commands.UnhideTalk
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_lore(Lore: Any, ) -> event_commands.AddLore:
    command_t = event_commands.AddLore
    parameters: dict[str, Any] = {"Lore": Lore}
    parameters = dict(filter(optional_value_filter(["Lore"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_lore(Lore: Any, ) -> event_commands.RemoveLore:
    command_t = event_commands.RemoveLore
    parameters: dict[str, Any] = {"Lore": Lore}
    parameters = dict(filter(optional_value_filter(["Lore"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_base_convo(Nid: Any, ) -> event_commands.AddBaseConvo:
    command_t = event_commands.AddBaseConvo
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def ignore_base_convo(Nid: Any, Ignore: Any = None, ) -> event_commands.IgnoreBaseConvo:
    command_t = event_commands.IgnoreBaseConvo
    parameters: dict[str, Any] = {"Nid": Nid, "Ignore": Ignore}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_base_convo(Nid: Any, ) -> event_commands.RemoveBaseConvo:
    command_t = event_commands.RemoveBaseConvo
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def increment_support_points(Unit1: Any, Unit2: Any, SupportPoints: Any, ) -> event_commands.IncrementSupportPoints:
    command_t = event_commands.IncrementSupportPoints
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2, "SupportPoints": SupportPoints}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2", "SupportPoints"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unlock_support_rank(Unit1: Any, Unit2: Any, SupportRank: Any, ) -> event_commands.UnlockSupportRank:
    command_t = event_commands.UnlockSupportRank
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2, "SupportRank": SupportRank}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2", "SupportRank"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def disable_support_rank(Unit1: Any, Unit2: Any, SupportRank: Any, ) -> event_commands.DisableSupportRank:
    command_t = event_commands.DisableSupportRank
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2, "SupportRank": SupportRank}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2", "SupportRank"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_market_item(Item: Any, Stock: Any = None, ) -> event_commands.AddMarketItem:
    command_t = event_commands.AddMarketItem
    parameters: dict[str, Any] = {"Item": Item, "Stock": Stock}
    parameters = dict(filter(optional_value_filter(["Item"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_market_item(Item: Any, Stock: Any = None, ) -> event_commands.RemoveMarketItem:
    command_t = event_commands.RemoveMarketItem
    parameters: dict[str, Any] = {"Item": Item, "Stock": Stock}
    parameters = dict(filter(optional_value_filter(["Item"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def clear_market_items() -> event_commands.ClearMarketItems:
    command_t = event_commands.ClearMarketItems
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def dump_vars() -> event_commands.DumpVars:
    command_t = event_commands.DumpVars
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_region(Region: Any, Position: Any, Size: Any, RegionType: Any, String: Any = None, TimeLeft: Any = None, HideTime: Any = None, Highlight: Any = None, ) -> event_commands.AddRegion:
    command_t = event_commands.AddRegion
    parameters: dict[str, Any] = {"Region": Region, "Position": Position, "Size": Size, "RegionType": RegionType, "String": String, "TimeLeft": TimeLeft, "HideTime": HideTime, "Highlight": Highlight}
    parameters = dict(filter(optional_value_filter(["Region", "Position", "Size", "RegionType"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def region_condition(Region: Any, Expression: Any, ) -> event_commands.RegionCondition:
    command_t = event_commands.RegionCondition
    parameters: dict[str, Any] = {"Region": Region, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Region", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_region(Region: Any, ) -> event_commands.RemoveRegion:
    command_t = event_commands.RemoveRegion
    parameters: dict[str, Any] = {"Region": Region}
    parameters = dict(filter(optional_value_filter(["Region"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_generics_from_region(Nid: Any, ) -> event_commands.RemoveGenericsFromRegion:
    command_t = event_commands.RemoveGenericsFromRegion
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def show_layer(Layer: Any, LayerTransition: Any = None, ) -> event_commands.ShowLayer:
    command_t = event_commands.ShowLayer
    parameters: dict[str, Any] = {"Layer": Layer, "LayerTransition": LayerTransition}
    parameters = dict(filter(optional_value_filter(["Layer"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def hide_layer(Layer: Any, LayerTransition: Any = None, ) -> event_commands.HideLayer:
    command_t = event_commands.HideLayer
    parameters: dict[str, Any] = {"Layer": Layer, "LayerTransition": LayerTransition}
    parameters = dict(filter(optional_value_filter(["Layer"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_weather(Weather: Any, Position: Any = None, ) -> event_commands.AddWeather:
    command_t = event_commands.AddWeather
    parameters: dict[str, Any] = {"Weather": Weather, "Position": Position}
    parameters = dict(filter(optional_value_filter(["Weather"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_weather(Weather: Any, Position: Any = None, ) -> event_commands.RemoveWeather:
    command_t = event_commands.RemoveWeather
    parameters: dict[str, Any] = {"Weather": Weather, "Position": Position}
    parameters = dict(filter(optional_value_filter(["Weather"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_objective_simple(EvaluableString: Any = None, ) -> event_commands.ChangeObjectiveSimple:
    command_t = event_commands.ChangeObjectiveSimple
    parameters: dict[str, Any] = {"EvaluableString": EvaluableString}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_objective_win(EvaluableString: Any, ) -> event_commands.ChangeObjectiveWin:
    command_t = event_commands.ChangeObjectiveWin
    parameters: dict[str, Any] = {"EvaluableString": EvaluableString}
    parameters = dict(filter(optional_value_filter(["EvaluableString"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_objective_loss(EvaluableString: Any, ) -> event_commands.ChangeObjectiveLoss:
    command_t = event_commands.ChangeObjectiveLoss
    parameters: dict[str, Any] = {"EvaluableString": EvaluableString}
    parameters = dict(filter(optional_value_filter(["EvaluableString"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_position(Position: Any, ) -> event_commands.SetPosition:
    command_t = event_commands.SetPosition
    parameters: dict[str, Any] = {"Position": Position}
    parameters = dict(filter(optional_value_filter(["Position"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def map_anim(MapAnim: Any, FloatPosition: Any, Speed: Any = None, ) -> event_commands.MapAnim:
    command_t = event_commands.MapAnim
    parameters: dict[str, Any] = {"MapAnim": MapAnim, "FloatPosition": FloatPosition, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["MapAnim", "FloatPosition"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_map_anim(MapAnim: Any, FloatPosition: Any, ) -> event_commands.RemoveMapAnim:
    command_t = event_commands.RemoveMapAnim
    parameters: dict[str, Any] = {"MapAnim": MapAnim, "FloatPosition": FloatPosition}
    parameters = dict(filter(optional_value_filter(["MapAnim", "FloatPosition"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_unit_map_anim(MapAnim: Any, Unit: Any, Speed: Any = None, ) -> event_commands.AddUnitMapAnim:
    command_t = event_commands.AddUnitMapAnim
    parameters: dict[str, Any] = {"MapAnim": MapAnim, "Unit": Unit, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["MapAnim", "Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_unit_map_anim(MapAnim: Any, Unit: Any, ) -> event_commands.RemoveUnitMapAnim:
    command_t = event_commands.RemoveUnitMapAnim
    parameters: dict[str, Any] = {"MapAnim": MapAnim, "Unit": Unit}
    parameters = dict(filter(optional_value_filter(["MapAnim", "Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_unit_marker(Unit: Any, MarkerNid: Any, Sound: Any = None, Time: Any = None, ) -> event_commands.AddUnitMarker:
    command_t = event_commands.AddUnitMarker
    parameters: dict[str, Any] = {"Unit": Unit, "MarkerNid": MarkerNid, "Sound": Sound, "Time": Time}
    parameters = dict(filter(optional_value_filter(["Unit", "MarkerNid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_unit_marker(Unit: Any, ) -> event_commands.RemoveUnitMarker:
    command_t = event_commands.RemoveUnitMarker
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def merge_parties(Party1: Any, Party2: Any, ) -> event_commands.MergeParties:
    command_t = event_commands.MergeParties
    parameters: dict[str, Any] = {"Party1": Party1, "Party2": Party2}
    parameters = dict(filter(optional_value_filter(["Party1", "Party2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def arrange_formation() -> event_commands.ArrangeFormation:
    command_t = event_commands.ArrangeFormation
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def prep(PickUnitsEnabled: Any = None, Music: Any = None, OtherOptions: Any = None, OtherOptionsEnabled: Any = None, OtherOptionsOnSelect: Any = None, OtherOptionsDescription: Any = None, ) -> event_commands.Prep:
    command_t = event_commands.Prep
    parameters: dict[str, Any] = {"PickUnitsEnabled": PickUnitsEnabled, "Music": Music, "OtherOptions": OtherOptions, "OtherOptionsEnabled": OtherOptionsEnabled, "OtherOptionsOnSelect": OtherOptionsOnSelect, "OtherOptionsDescription": OtherOptionsDescription}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def base(Background: Any, Music: Any = None, OtherOptions: Any = None, OtherOptionsEnabled: Any = None, OtherOptionsOnSelect: Any = None, ) -> event_commands.Base:
    command_t = event_commands.Base
    parameters: dict[str, Any] = {"Background": Background, "Music": Music, "OtherOptions": OtherOptions, "OtherOptionsEnabled": OtherOptionsEnabled, "OtherOptionsOnSelect": OtherOptionsOnSelect}
    parameters = dict(filter(optional_value_filter(["Background"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_custom_options(CustomOptions: Any, CustomOptionsEnabled: Any = None, CustomOptionsDesc: Any = None, CustomOptionsOnSelect: Any = None, ) -> event_commands.SetCustomOptions:
    command_t = event_commands.SetCustomOptions
    parameters: dict[str, Any] = {"CustomOptions": CustomOptions, "CustomOptionsEnabled": CustomOptionsEnabled, "CustomOptionsDesc": CustomOptionsDesc, "CustomOptionsOnSelect": CustomOptionsOnSelect}
    parameters = dict(filter(optional_value_filter(["CustomOptions"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def shop(Unit: Any, ItemList: Any, ShopFlavor: Any = None, StockList: Any = None, ShopId: Any = None, ) -> event_commands.Shop:
    command_t = event_commands.Shop
    parameters: dict[str, Any] = {"Unit": Unit, "ItemList": ItemList, "ShopFlavor": ShopFlavor, "StockList": StockList, "ShopId": ShopId}
    parameters = dict(filter(optional_value_filter(["Unit", "ItemList"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def choice(Nid: Any, Title: Any, Choices: Any, RowWidth: Any = None, Orientation: Any = None, Alignment: Any = None, BG: Any = None, EventNid: Any = None, EntryType: Any = None, Dimensions: Any = None, TextAlign: Any = None, ) -> event_commands.Choice:
    command_t = event_commands.Choice
    parameters: dict[str, Any] = {"Nid": Nid, "Title": Title, "Choices": Choices, "RowWidth": RowWidth, "Orientation": Orientation, "Alignment": Alignment, "BG": BG, "EventNid": EventNid, "EntryType": EntryType, "Dimensions": Dimensions, "TextAlign": TextAlign}
    parameters = dict(filter(optional_value_filter(["Nid", "Title", "Choices"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unchoice() -> event_commands.Unchoice:
    command_t = event_commands.Unchoice
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def textbox(NID: Any, Text: Any, BoxPosition: Any = None, Width: Any = None, NumLines: Any = None, StyleNid: Any = None, TextSpeed: Any = None, FontColor: Any = None, FontType: Any = None, BG: Any = None, ) -> event_commands.Textbox:
    command_t = event_commands.Textbox
    parameters: dict[str, Any] = {"NID": NID, "Text": Text, "BoxPosition": BoxPosition, "Width": Width, "NumLines": NumLines, "StyleNid": StyleNid, "TextSpeed": TextSpeed, "FontColor": FontColor, "FontType": FontType, "BG": BG}
    parameters = dict(filter(optional_value_filter(["NID", "Text"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def table(Nid: Any, TableData: Any, Title: Any = None, Dimensions: Any = None, RowWidth: Any = None, Alignment: Any = None, BG: Any = None, EntryType: Any = None, TextAlign: Any = None, ) -> event_commands.Table:
    command_t = event_commands.Table
    parameters: dict[str, Any] = {"Nid": Nid, "TableData": TableData, "Title": Title, "Dimensions": Dimensions, "RowWidth": RowWidth, "Alignment": Alignment, "BG": BG, "EntryType": EntryType, "TextAlign": TextAlign}
    parameters = dict(filter(optional_value_filter(["Nid", "TableData"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_table(Nid: Any, ) -> event_commands.RemoveTable:
    command_t = event_commands.RemoveTable
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def text_entry(Nid: Any, String: Any, CharacterLimit: Any = None, IllegalCharacterList: Any = None, DefaultString: Any = None, MinimumCharacterLimit: Any = None, ) -> event_commands.TextEntry:
    command_t = event_commands.TextEntry
    parameters: dict[str, Any] = {"Nid": Nid, "String": String, "CharacterLimit": CharacterLimit, "IllegalCharacterList": IllegalCharacterList, "DefaultString": DefaultString, "MinimumCharacterLimit": MinimumCharacterLimit}
    parameters = dict(filter(optional_value_filter(["Nid", "String"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def chapter_title(Music: Any = None, String: Any = None, ) -> event_commands.ChapterTitle:
    command_t = event_commands.ChapterTitle
    parameters: dict[str, Any] = {"Music": Music, "String": String}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def draw_overlay_sprite(Nid: Any, SpriteID: Any, Position: Any = None, ZLevel: Any = None, Animation: Any = None, Speed: Any = None, ) -> event_commands.DrawOverlaySprite:
    command_t = event_commands.DrawOverlaySprite
    parameters: dict[str, Any] = {"Nid": Nid, "SpriteID": SpriteID, "Position": Position, "ZLevel": ZLevel, "Animation": Animation, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Nid", "SpriteID"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_overlay_sprite(Nid: Any, Animation: Any = None, Speed: Any = None, ) -> event_commands.RemoveOverlaySprite:
    command_t = event_commands.RemoveOverlaySprite
    parameters: dict[str, Any] = {"Nid": Nid, "Animation": Animation, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def alert(String: Any, Item: Any = None, Skill: Any = None, Icon: Any = None, ) -> event_commands.Alert:
    command_t = event_commands.Alert
    parameters: dict[str, Any] = {"String": String, "Item": Item, "Skill": Skill, "Icon": Icon}
    parameters = dict(filter(optional_value_filter(["String"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def victory_screen(Sound: Any = None, ) -> event_commands.VictoryScreen:
    command_t = event_commands.VictoryScreen
    parameters: dict[str, Any] = {"Sound": Sound}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def records_screen() -> event_commands.RecordsScreen:
    command_t = event_commands.RecordsScreen
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def open_library() -> event_commands.OpenLibrary:
    command_t = event_commands.OpenLibrary
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def open_guide() -> event_commands.OpenGuide:
    command_t = event_commands.OpenGuide
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def open_credits(Panorama: Any = None, ) -> event_commands.OpenCredits:
    command_t = event_commands.OpenCredits
    parameters: dict[str, Any] = {"Panorama": Panorama}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def open_unit_management(Panorama: Any = None, ) -> event_commands.OpenUnitManagement:
    command_t = event_commands.OpenUnitManagement
    parameters: dict[str, Any] = {"Panorama": Panorama}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def open_trade(Unit1: Any, Unit2: Any, ) -> event_commands.OpenTrade:
    command_t = event_commands.OpenTrade
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def open_bexp_menu(Panorama: Any = None, Music: Any = None, ) -> event_commands.OpenBexpMenu:
    command_t = event_commands.OpenBexpMenu
    parameters: dict[str, Any] = {"Panorama": Panorama, "Music": Music}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def show_minimap() -> event_commands.ShowMinimap:
    command_t = event_commands.ShowMinimap
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def open_achievements(Background: Any, ) -> event_commands.OpenAchievements:
    command_t = event_commands.OpenAchievements
    parameters: dict[str, Any] = {"Background": Background}
    parameters = dict(filter(optional_value_filter(["Background"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def soundroom(Panorama: Any = None, ) -> event_commands.Soundroom:
    command_t = event_commands.Soundroom
    parameters: dict[str, Any] = {"Panorama": Panorama}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def location_card(String: Any, ) -> event_commands.LocationCard:
    command_t = event_commands.LocationCard
    parameters: dict[str, Any] = {"String": String}
    parameters = dict(filter(optional_value_filter(["String"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def credits(Role: Any, Credits: Any, ) -> event_commands.Credits:
    command_t = event_commands.Credits
    parameters: dict[str, Any] = {"Role": Role, "Credits": Credits}
    parameters = dict(filter(optional_value_filter(["Role", "Credits"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def ending(Portrait: Any, Title: Any, Text: Any, ) -> event_commands.Ending:
    command_t = event_commands.Ending
    parameters: dict[str, Any] = {"Portrait": Portrait, "Title": Title, "Text": Text}
    parameters = dict(filter(optional_value_filter(["Portrait", "Title", "Text"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def paired_ending(LeftPortrait: Any, RightPortrait: Any, LeftTitle: Any, RightTitle: Any, Text: Any, ) -> event_commands.PairedEnding:
    command_t = event_commands.PairedEnding
    parameters: dict[str, Any] = {"LeftPortrait": LeftPortrait, "RightPortrait": RightPortrait, "LeftTitle": LeftTitle, "RightTitle": RightTitle, "Text": Text}
    parameters = dict(filter(optional_value_filter(["LeftPortrait", "RightPortrait", "LeftTitle", "RightTitle", "Text"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def pop_dialog() -> event_commands.PopDialog:
    command_t = event_commands.PopDialog
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unlock(Unit: Any, ) -> event_commands.Unlock:
    command_t = event_commands.Unlock
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def trigger_script(Event: Any, Unit1: Any = None, Unit2: Any = None, ) -> event_commands.TriggerScript:
    command_t = event_commands.TriggerScript
    parameters: dict[str, Any] = {"Event": Event, "Unit1": Unit1, "Unit2": Unit2}
    parameters = dict(filter(optional_value_filter(["Event"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def trigger_script_with_args(Event: Any, ArgList: Any = None, ) -> event_commands.TriggerScriptWithArgs:
    command_t = event_commands.TriggerScriptWithArgs
    parameters: dict[str, Any] = {"Event": Event, "ArgList": ArgList}
    parameters = dict(filter(optional_value_filter(["Event"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_roaming(FreeRoamEnabled: Any, ) -> event_commands.ChangeRoaming:
    command_t = event_commands.ChangeRoaming
    parameters: dict[str, Any] = {"FreeRoamEnabled": FreeRoamEnabled}
    parameters = dict(filter(optional_value_filter(["FreeRoamEnabled"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_roaming_unit(Unit: Any, ) -> event_commands.ChangeRoamingUnit:
    command_t = event_commands.ChangeRoamingUnit
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def clean_up_roaming() -> event_commands.CleanUpRoaming:
    command_t = event_commands.CleanUpRoaming
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_to_initiative(Unit: Any, Integer: Any, ) -> event_commands.AddToInitiative:
    command_t = event_commands.AddToInitiative
    parameters: dict[str, Any] = {"Unit": Unit, "Integer": Integer}
    parameters = dict(filter(optional_value_filter(["Unit", "Integer"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def move_in_initiative(Unit: Any, Integer: Any, ) -> event_commands.MoveInInitiative:
    command_t = event_commands.MoveInInitiative
    parameters: dict[str, Any] = {"Unit": Unit, "Integer": Integer}
    parameters = dict(filter(optional_value_filter(["Unit", "Integer"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def pair_up(Unit1: Any, Unit2: Any, ) -> event_commands.PairUp:
    command_t = event_commands.PairUp
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def separate(Unit: Any, ) -> event_commands.Separate:
    command_t = event_commands.Separate
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def overworld_cinematic(OverworldNID: Any = None, ) -> event_commands.OverworldCinematic:
    command_t = event_commands.OverworldCinematic
    parameters: dict[str, Any] = {"OverworldNID": OverworldNID}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_overworld_position(OverworldEntity: Any, OverworldLocation: Any, ) -> event_commands.SetOverworldPosition:
    command_t = event_commands.SetOverworldPosition
    parameters: dict[str, Any] = {"OverworldEntity": OverworldEntity, "OverworldLocation": OverworldLocation}
    parameters = dict(filter(optional_value_filter(["OverworldEntity", "OverworldLocation"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def overworld_move_unit(OverworldEntity: Any, OverworldLocation: Any = None, Speed: Any = None, PointList: Any = None, ) -> event_commands.OverworldMoveUnit:
    command_t = event_commands.OverworldMoveUnit
    parameters: dict[str, Any] = {"OverworldEntity": OverworldEntity, "OverworldLocation": OverworldLocation, "Speed": Speed, "PointList": PointList}
    parameters = dict(filter(optional_value_filter(["OverworldEntity"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def reveal_overworld_node(OverworldNodeNid: Any, ) -> event_commands.RevealOverworldNode:
    command_t = event_commands.RevealOverworldNode
    parameters: dict[str, Any] = {"OverworldNodeNid": OverworldNodeNid}
    parameters = dict(filter(optional_value_filter(["OverworldNodeNid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def reveal_overworld_road(Node1: Any, Node2: Any, ) -> event_commands.RevealOverworldRoad:
    command_t = event_commands.RevealOverworldRoad
    parameters: dict[str, Any] = {"Node1": Node1, "Node2": Node2}
    parameters = dict(filter(optional_value_filter(["Node1", "Node2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def create_overworld_entity(Nid: Any, Unit: Any = None, Team: Any = None, ) -> event_commands.CreateOverworldEntity:
    command_t = event_commands.CreateOverworldEntity
    parameters: dict[str, Any] = {"Nid": Nid, "Unit": Unit, "Team": Team}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def disable_overworld_entity(Nid: Any, ) -> event_commands.DisableOverworldEntity:
    command_t = event_commands.DisableOverworldEntity
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def toggle_narration_mode(Direction: Any, Speed: Any = None, ) -> event_commands.ToggleNarrationMode:
    command_t = event_commands.ToggleNarrationMode
    parameters: dict[str, Any] = {"Direction": Direction, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Direction"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def hide_combat_ui() -> event_commands.HideCombatUI:
    command_t = event_commands.HideCombatUI
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def show_combat_ui() -> event_commands.ShowCombatUI:
    command_t = event_commands.ShowCombatUI
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_overworld_menu_option_enabled(OverworldNID: Any, OverworldNodeNid: Any, OverworldNodeMenuOption: Any, Setting: Any, ) -> event_commands.SetOverworldMenuOptionEnabled:
    command_t = event_commands.SetOverworldMenuOptionEnabled
    parameters: dict[str, Any] = {"OverworldNID": OverworldNID, "OverworldNodeNid": OverworldNodeNid, "OverworldNodeMenuOption": OverworldNodeMenuOption, "Setting": Setting}
    parameters = dict(filter(optional_value_filter(["OverworldNID", "OverworldNodeNid", "OverworldNodeMenuOption", "Setting"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_overworld_menu_option_visible(OverworldNID: Any, OverworldNodeNID: Any, OverworldNodeMenuOption: Any, Setting: Any, ) -> event_commands.SetOverworldMenuOptionVisible:
    command_t = event_commands.SetOverworldMenuOptionVisible
    parameters: dict[str, Any] = {"OverworldNID": OverworldNID, "OverworldNodeNID": OverworldNodeNID, "OverworldNodeMenuOption": OverworldNodeMenuOption, "Setting": Setting}
    parameters = dict(filter(optional_value_filter(["OverworldNID", "OverworldNodeNID", "OverworldNodeMenuOption", "Setting"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def enter_level_from_overworld(LevelNid: Any, ) -> event_commands.EnterLevelFromOverworld:
    command_t = event_commands.EnterLevelFromOverworld
    parameters: dict[str, Any] = {"LevelNid": LevelNid}
    parameters = dict(filter(optional_value_filter(["LevelNid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def create_achievement(Nid: Any, Name: Any, Description: Any, ) -> event_commands.CreateAchievement:
    command_t = event_commands.CreateAchievement
    parameters: dict[str, Any] = {"Nid": Nid, "Name": Name, "Description": Description}
    parameters = dict(filter(optional_value_filter(["Nid", "Name", "Description"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def update_achievement(Achievement: Any, Name: Any, Description: Any, ) -> event_commands.UpdateAchievement:
    command_t = event_commands.UpdateAchievement
    parameters: dict[str, Any] = {"Achievement": Achievement, "Name": Name, "Description": Description}
    parameters = dict(filter(optional_value_filter(["Achievement", "Name", "Description"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def complete_achievement(Achievement: Any, Completed: Any, ) -> event_commands.CompleteAchievement:
    command_t = event_commands.CompleteAchievement
    parameters: dict[str, Any] = {"Achievement": Achievement, "Completed": Completed}
    parameters = dict(filter(optional_value_filter(["Achievement", "Completed"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def clear_achievements() -> event_commands.ClearAchievements:
    command_t = event_commands.ClearAchievements
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def create_record(Nid: Any, Expression: Any, ) -> event_commands.CreateRecord:
    command_t = event_commands.CreateRecord
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def update_record(Nid: Any, Expression: Any, ) -> event_commands.UpdateRecord:
    command_t = event_commands.UpdateRecord
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def replace_record(Nid: Any, Expression: Any, ) -> event_commands.ReplaceRecord:
    command_t = event_commands.ReplaceRecord
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def delete_record(Nid: Any, ) -> event_commands.DeleteRecord:
    command_t = event_commands.DeleteRecord
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unlock_difficulty(DifficultyMode: Any, ) -> event_commands.UnlockDifficulty:
    command_t = event_commands.UnlockDifficulty
    parameters: dict[str, Any] = {"DifficultyMode": DifficultyMode}
    parameters = dict(filter(optional_value_filter(["DifficultyMode"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unlock_song(Music: Any, ) -> event_commands.UnlockSong:
    command_t = event_commands.UnlockSong
    parameters: dict[str, Any] = {"Music": Music}
    parameters = dict(filter(optional_value_filter(["Music"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unlock_support_room() -> event_commands.UnlockSupportRoom:
    command_t = event_commands.UnlockSupportRoom
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def party_transfer(Party1: Any, Party2: Any, FixedUnits: Any = None, Party1Name: Any = None, Party2Name: Any = None, Party1Limit: Any = None, Party2Limit: Any = None, ) -> event_commands.PartyTransfer:
    command_t = event_commands.PartyTransfer
    parameters: dict[str, Any] = {"Party1": Party1, "Party2": Party2, "FixedUnits": FixedUnits, "Party1Name": Party1Name, "Party2Name": Party2Name, "Party1Limit": Party1Limit, "Party2Limit": Party2Limit}
    parameters = dict(filter(optional_value_filter(["Party1", "Party2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def change_team_palette(Team: Any, MapSpritePalette: Any = None, CombatVariantPalette: Any = None, CombatColor: Any = None, ) -> event_commands.ChangeTeamPalette:
    command_t = event_commands.ChangeTeamPalette
    parameters: dict[str, Any] = {"Team": Team, "MapSpritePalette": MapSpritePalette, "CombatVariantPalette": CombatVariantPalette, "CombatColor": CombatColor}
    parameters = dict(filter(optional_value_filter(["Team"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def chest_loot_item(GlobalUnitOrConvoy: Any, Item: Any, ) -> event_commands.ChestLootItem:
    command_t = event_commands.ChestLootItem
    parameters: dict[str, Any] = {"GlobalUnitOrConvoy": GlobalUnitOrConvoy, "Item": Item}
    parameters = dict(filter(optional_value_filter(["GlobalUnitOrConvoy", "Item"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def clear_map_anims() -> event_commands.ClearMapAnims:
    command_t = event_commands.ClearMapAnims
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_difficulty_mode(DifficultyMode: Any, ) -> event_commands.SetDifficultyMode:
    command_t = event_commands.SetDifficultyMode
    parameters: dict[str, Any] = {"DifficultyMode": DifficultyMode}
    parameters = dict(filter(optional_value_filter(["DifficultyMode"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_game_rules(Ruleset: Any, ) -> event_commands.SetGameRules:
    command_t = event_commands.SetGameRules
    parameters: dict[str, Any] = {"Ruleset": Ruleset}
    parameters = dict(filter(optional_value_filter(["Ruleset"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def upgrade_personal_skill_t2(GlobalUnit: Any, ) -> event_commands.UpgradePersonalSkillT2:
    command_t = event_commands.UpgradePersonalSkillT2
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit}
    parameters = dict(filter(optional_value_filter(["GlobalUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def upgrade_personal_skill_t3(GlobalUnit: Any, ) -> event_commands.UpgradePersonalSkillT3:
    command_t = event_commands.UpgradePersonalSkillT3
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit}
    parameters = dict(filter(optional_value_filter(["GlobalUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def restore_status(GlobalUnit: Any, ) -> event_commands.RestoreStatus:
    command_t = event_commands.RestoreStatus
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit}
    parameters = dict(filter(optional_value_filter(["GlobalUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def heal_unit(GlobalUnit: Any, Integer: Any, ) -> event_commands.HealUnit:
    command_t = event_commands.HealUnit
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Integer": Integer}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Integer"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def clear_portraits() -> event_commands.ClearPortraits:
    command_t = event_commands.ClearPortraits
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def wipe_weapon_type(GlobalUnit: Any, WeaponType: Any, ) -> event_commands.WipeWeaponType:
    command_t = event_commands.WipeWeaponType
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "WeaponType": WeaponType}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "WeaponType"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_level(GlobalUnit: Any, Integer: Any, ) -> event_commands.SetLevel:
    command_t = event_commands.SetLevel
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Integer": Integer}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Integer"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unload_unit(UniqueUnit: Any, ) -> event_commands.UnloadUnit:
    command_t = event_commands.UnloadUnit
    parameters: dict[str, Any] = {"UniqueUnit": UniqueUnit}
    parameters = dict(filter(optional_value_filter(["UniqueUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def store_regions() -> event_commands.StoreRegions:
    command_t = event_commands.StoreRegions
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def recall_regions() -> event_commands.RecallRegions:
    command_t = event_commands.RecallRegions
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def force_skill_tutorial(Unit: Any, ) -> event_commands.ForceSkillTutorial:
    command_t = event_commands.ForceSkillTutorial
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def restrict_keys(Keys: Any, ) -> event_commands.RestrictKeys:
    command_t = event_commands.RestrictKeys
    parameters: dict[str, Any] = {"Keys": Keys}
    parameters = dict(filter(optional_value_filter(["Keys"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unrestrict_keys() -> event_commands.UnrestrictKeys:
    command_t = event_commands.UnrestrictKeys
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def draw_hand(Nid: Any, TopLeft: Any, Size: Any = None, EndAfter: Any = None, ) -> event_commands.DrawHand:
    command_t = event_commands.DrawHand
    parameters: dict[str, Any] = {"Nid": Nid, "TopLeft": TopLeft, "Size": Size, "EndAfter": EndAfter}
    parameters = dict(filter(optional_value_filter(["Nid", "TopLeft"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def draw_highlight(Nid: Any, TopLeft: Any, Size: Any = None, Color: Any = None, EndAfter: Any = None, ) -> event_commands.DrawHighlight:
    command_t = event_commands.DrawHighlight
    parameters: dict[str, Any] = {"Nid": Nid, "TopLeft": TopLeft, "Size": Size, "Color": Color, "EndAfter": EndAfter}
    parameters = dict(filter(optional_value_filter(["Nid", "TopLeft"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove_overlay(Nid: Any = None, ) -> event_commands.RemoveOverlay:
    command_t = event_commands.RemoveOverlay
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def force_movement(Units: Any, Positions: Any, RejectText: Any = None, ) -> event_commands.ForceMovement:
    command_t = event_commands.ForceMovement
    parameters: dict[str, Any] = {"Units": Units, "Positions": Positions, "RejectText": RejectText}
    parameters = dict(filter(optional_value_filter(["Units", "Positions"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def release_forced_movement() -> event_commands.ReleaseForcedMovement:
    command_t = event_commands.ReleaseForcedMovement
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_unit_menu_options(Unit: Any, Options: Any, ) -> event_commands.SetUnitMenuOptions:
    command_t = event_commands.SetUnitMenuOptions
    parameters: dict[str, Any] = {"Unit": Unit, "Options": Options}
    parameters = dict(filter(optional_value_filter(["Unit", "Options"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def clear_unit_menu_options(Unit: Any, ) -> event_commands.ClearUnitMenuOptions:
    command_t = event_commands.ClearUnitMenuOptions
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def m(Music: Any, FadeIn: Any = None, ) -> event_commands.Music:
    command_t = event_commands.Music
    parameters: dict[str, Any] = {"Music": Music, "FadeIn": FadeIn}
    parameters = dict(filter(optional_value_filter(["Music"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def mf(FadeOut: Any = None, ) -> event_commands.MusicFadeBack:
    command_t = event_commands.MusicFadeBack
    parameters: dict[str, Any] = {"FadeOut": FadeOut}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def u(Portrait: Any, ScreenPosition: Any, Slide: Any = None, ExpressionList: Any = None, SpeedMult: Any = None, ) -> event_commands.AddPortrait:
    command_t = event_commands.AddPortrait
    parameters: dict[str, Any] = {"Portrait": Portrait, "ScreenPosition": ScreenPosition, "Slide": Slide, "ExpressionList": ExpressionList, "SpeedMult": SpeedMult}
    parameters = dict(filter(optional_value_filter(["Portrait", "ScreenPosition"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def uu(Portrait1: Any, ScreenPosition1: Any, Portrait2: Any, ScreenPosition2: Any, Portrait3: Any = None, ScreenPosition3: Any = None, Portrait4: Any = None, ScreenPosition4: Any = None, ) -> event_commands.MultiAddPortrait:
    command_t = event_commands.MultiAddPortrait
    parameters: dict[str, Any] = {"Portrait1": Portrait1, "ScreenPosition1": ScreenPosition1, "Portrait2": Portrait2, "ScreenPosition2": ScreenPosition2, "Portrait3": Portrait3, "ScreenPosition3": ScreenPosition3, "Portrait4": Portrait4, "ScreenPosition4": ScreenPosition4}
    parameters = dict(filter(optional_value_filter(["Portrait1", "ScreenPosition1", "Portrait2", "ScreenPosition2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def r(Portrait: Any, SpeedMult: Any = None, Slide: Any = None, ) -> event_commands.RemovePortrait:
    command_t = event_commands.RemovePortrait
    parameters: dict[str, Any] = {"Portrait": Portrait, "SpeedMult": SpeedMult, "Slide": Slide}
    parameters = dict(filter(optional_value_filter(["Portrait"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def rr(Portrait1: Any, Portrait2: Any, Portrait3: Any = None, Portrait4: Any = None, ) -> event_commands.MultiRemovePortrait:
    command_t = event_commands.MultiRemovePortrait
    parameters: dict[str, Any] = {"Portrait1": Portrait1, "Portrait2": Portrait2, "Portrait3": Portrait3, "Portrait4": Portrait4}
    parameters = dict(filter(optional_value_filter(["Portrait1", "Portrait2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def rrr() -> event_commands.RemoveAllPortraits:
    command_t = event_commands.RemoveAllPortraits
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def bop(Portrait: Any, NumBops: Any = None, Time: Any = None, ) -> event_commands.BopPortrait:
    command_t = event_commands.BopPortrait
    parameters: dict[str, Any] = {"Portrait": Portrait, "NumBops": NumBops, "Time": Time}
    parameters = dict(filter(optional_value_filter(["Portrait"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def mirror(Portrait: Any, SpeedMult: Any = None, ) -> event_commands.MirrorPortrait:
    command_t = event_commands.MirrorPortrait
    parameters: dict[str, Any] = {"Portrait": Portrait, "SpeedMult": SpeedMult}
    parameters = dict(filter(optional_value_filter(["Portrait"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def e(Portrait: Any, ExpressionList: Any, ) -> event_commands.Expression:
    command_t = event_commands.Expression
    parameters: dict[str, Any] = {"Portrait": Portrait, "ExpressionList": ExpressionList}
    parameters = dict(filter(optional_value_filter(["Portrait", "ExpressionList"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def s(SpeakerOrStyle: Any, *Text: Any, TextPosition: Any = None, Width: Any = None, StyleNid: Any = None, TextSpeed: Any = None, FontColor: Any = None, FontType: Any = None, DialogBox: Any = None, NumLines: Any = None, DrawCursor: Any = None, MessageTail: Any = None, Transparency: Any = None, NameTagBg: Any = None, BoopSound: Any = None, ) -> event_commands.Say:
    command_t = event_commands.Say
    parameters: dict[str, Any] = {"SpeakerOrStyle": SpeakerOrStyle, "Text": Text, "TextPosition": TextPosition, "Width": Width, "StyleNid": StyleNid, "TextSpeed": TextSpeed, "FontColor": FontColor, "FontType": FontType, "DialogBox": DialogBox, "NumLines": NumLines, "DrawCursor": DrawCursor, "MessageTail": MessageTail, "Transparency": Transparency, "NameTagBg": NameTagBg, "BoopSound": BoopSound}
    parameters = dict(filter(optional_value_filter(["SpeakerOrStyle", "*Text"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def t(Direction: Any = None, Speed: Any = None, Color3: Any = None, Panorama: Any = None, ) -> event_commands.Transition:
    command_t = event_commands.Transition
    parameters: dict[str, Any] = {"Direction": Direction, "Speed": Speed, "Color3": Color3, "Panorama": Panorama}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def b(Panorama: Any = None, Speed: Any = None, ) -> event_commands.ChangeBackground:
    command_t = event_commands.ChangeBackground
    parameters: dict[str, Any] = {"Panorama": Panorama, "Speed": Speed}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_cursor(Position: Any, Speed: Any = None, ) -> event_commands.MoveCursor:
    command_t = event_commands.MoveCursor
    parameters: dict[str, Any] = {"Position": Position, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Position"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def camera_path(Positions: Any, TotalSpeed: Any = None, TilesPerSecond: Any = None, Music: Any = None, ) -> event_commands.SmoothCameraPath:
    command_t = event_commands.SmoothCameraPath
    parameters: dict[str, Any] = {"Positions": Positions, "TotalSpeed": TotalSpeed, "TilesPerSecond": TilesPerSecond, "Music": Music}
    parameters = dict(filter(optional_value_filter(["Positions"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def highlight(Position: Any, ) -> event_commands.FlickerCursor:
    command_t = event_commands.FlickerCursor
    parameters: dict[str, Any] = {"Position": Position}
    parameters = dict(filter(optional_value_filter(["Position"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def gvar(Nid: Any, Expression: Any, ) -> event_commands.GameVar:
    command_t = event_commands.GameVar
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def ginc(Nid: Any, Expression: Any = None, ) -> event_commands.IncGameVar:
    command_t = event_commands.IncGameVar
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def lvar(Nid: Any, Expression: Any, ) -> event_commands.LevelVar:
    command_t = event_commands.LevelVar
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid", "Expression"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def linc(Nid: Any, Expression: Any = None, ) -> event_commands.IncLevelVar:
    command_t = event_commands.IncLevelVar
    parameters: dict[str, Any] = {"Nid": Nid, "Expression": Expression}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add(Unit: Any, Position: Any = None, EntryType: Any = None, Placement: Any = None, AnimationType: Any = None, ) -> event_commands.AddUnit:
    command_t = event_commands.AddUnit
    parameters: dict[str, Any] = {"Unit": Unit, "Position": Position, "EntryType": EntryType, "Placement": Placement, "AnimationType": AnimationType}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def move(Unit: Any, Position: Any = None, MovementType: Any = None, Placement: Any = None, Speed: Any = None, ) -> event_commands.MoveUnit:
    command_t = event_commands.MoveUnit
    parameters: dict[str, Any] = {"Unit": Unit, "Position": Position, "MovementType": MovementType, "Placement": Placement, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def remove(Unit: Any, RemoveType: Any = None, AnimationType: Any = None, ) -> event_commands.RemoveUnit:
    command_t = event_commands.RemoveUnit
    parameters: dict[str, Any] = {"Unit": Unit, "RemoveType": RemoveType, "AnimationType": AnimationType}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def kill(Unit: Any, ) -> event_commands.KillUnit:
    command_t = event_commands.KillUnit
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def interact(Unit: Any, Position: Any, CombatScript: Any = None, Ability: Any = None, Rounds: Any = None, ) -> event_commands.InteractUnit:
    command_t = event_commands.InteractUnit
    parameters: dict[str, Any] = {"Unit": Unit, "Position": Position, "CombatScript": CombatScript, "Ability": Ability, "Rounds": Rounds}
    parameters = dict(filter(optional_value_filter(["Unit", "Position"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def resurrect_unit(GlobalUnit: Any, ) -> event_commands.Resurrect:
    command_t = event_commands.Resurrect
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit}
    parameters = dict(filter(optional_value_filter(["GlobalUnit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def reset_unit(Unit: Any, ) -> event_commands.Reset:
    command_t = event_commands.Reset
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def morph_group(Group: Any, StartingGroup: Any, MovementType: Any = None, Placement: Any = None, ) -> event_commands.MoveGroup:
    command_t = event_commands.MoveGroup
    parameters: dict[str, Any] = {"Group": Group, "StartingGroup": StartingGroup, "MovementType": MovementType, "Placement": Placement}
    parameters = dict(filter(optional_value_filter(["Group", "StartingGroup"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def add_skill(GlobalUnit: Any, Skill: Any, Initiator: Any = None, ) -> event_commands.GiveSkill:
    command_t = event_commands.GiveSkill
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "Skill": Skill, "Initiator": Initiator}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "Skill"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_ai(GlobalUnit: Any, AI: Any, ) -> event_commands.ChangeAI:
    command_t = event_commands.ChangeAI
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "AI": AI}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "AI"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_roam_ai(GlobalUnit: Any, AI: Any, ) -> event_commands.ChangeRoamAI:
    command_t = event_commands.ChangeRoamAI
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "AI": AI}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "AI"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def set_ai_group(GlobalUnit: Any, AIGroup: Any, ) -> event_commands.ChangeAIGroup:
    command_t = event_commands.ChangeAIGroup
    parameters: dict[str, Any] = {"GlobalUnit": GlobalUnit, "AIGroup": AIGroup}
    parameters = dict(filter(optional_value_filter(["GlobalUnit", "AIGroup"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unlock_lore(Lore: Any, ) -> event_commands.AddLore:
    command_t = event_commands.AddLore
    parameters: dict[str, Any] = {"Lore": Lore}
    parameters = dict(filter(optional_value_filter(["Lore"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def rmtable(Nid: Any, ) -> event_commands.RemoveTable:
    command_t = event_commands.RemoveTable
    parameters: dict[str, Any] = {"Nid": Nid}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def draw_overlay(Nid: Any, SpriteID: Any, Position: Any = None, ZLevel: Any = None, Animation: Any = None, Speed: Any = None, ) -> event_commands.DrawOverlaySprite:
    command_t = event_commands.DrawOverlaySprite
    parameters: dict[str, Any] = {"Nid": Nid, "SpriteID": SpriteID, "Position": Position, "ZLevel": ZLevel, "Animation": Animation, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Nid", "SpriteID"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def delete_overlay(Nid: Any, Animation: Any = None, Speed: Any = None, ) -> event_commands.RemoveOverlaySprite:
    command_t = event_commands.RemoveOverlaySprite
    parameters: dict[str, Any] = {"Nid": Nid, "Animation": Animation, "Speed": Speed}
    parameters = dict(filter(optional_value_filter(["Nid"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def rescue(Unit1: Any, Unit2: Any, ) -> event_commands.PairUp:
    command_t = event_commands.PairUp
    parameters: dict[str, Any] = {"Unit1": Unit1, "Unit2": Unit2}
    parameters = dict(filter(optional_value_filter(["Unit1", "Unit2"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def drop(Unit: Any, ) -> event_commands.Separate:
    command_t = event_commands.Separate
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def omove(OverworldEntity: Any, OverworldLocation: Any = None, Speed: Any = None, PointList: Any = None, ) -> event_commands.OverworldMoveUnit:
    command_t = event_commands.OverworldMoveUnit
    parameters: dict[str, Any] = {"OverworldEntity": OverworldEntity, "OverworldLocation": OverworldLocation, "Speed": Speed, "PointList": PointList}
    parameters = dict(filter(optional_value_filter(["OverworldEntity"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def skill_tutorial(Unit: Any, ) -> event_commands.ForceSkillTutorial:
    command_t = event_commands.ForceSkillTutorial
    parameters: dict[str, Any] = {"Unit": Unit}
    parameters = dict(filter(optional_value_filter(["Unit"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def lock_keys(Keys: Any, ) -> event_commands.RestrictKeys:
    command_t = event_commands.RestrictKeys
    parameters: dict[str, Any] = {"Keys": Keys}
    parameters = dict(filter(optional_value_filter(["Keys"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def unlock_keys() -> event_commands.UnrestrictKeys:
    command_t = event_commands.UnrestrictKeys
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def wait(Time: Any, ) -> event_commands.Wait:
    command_t = event_commands.Wait
    parameters: dict[str, Any] = {"Time": Time}
    parameters = dict(filter(optional_value_filter(["Time"]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def finish() -> event_commands.Finish:
    command_t = event_commands.Finish
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')

def end_skip() -> event_commands.EndSkip:
    command_t = event_commands.EndSkip
    parameters: dict[str, Any] = {}
    parameters = dict(filter(optional_value_filter([]), parameters.items()))
    for k, v in parameters.items():
        if isinstance(v, str):
            param_name = command_t.get_validator_from_keyword(k)
            if param_name is None:
                continue
            param_validator = event_validators.get(param_name)
            if param_validator and (
                issubclass(param_validator, event_validators.EnumValidator)
                or hasattr(param_validator, 'convert')
            ):
                try:
                    parameters[k] = event_validators.convert(param_name, v)
                except Exception:
                    pass
    return command_t(parameters=parameters).set_flags('from_python')
