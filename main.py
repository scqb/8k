def on_forever():
    basic.show_icon(IconNames.HEART)
    if cbit_小车类.Line_Sensor(cbit_小车类.enPos.LEFT_STATE, cbit_小车类.enLineState.BLACK) and cbit_小车类.Line_Sensor(cbit_小车类.enPos.RIGHT_STATE, cbit_小车类.enLineState.BLACK):
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
