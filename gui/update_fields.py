from gui.config import FieldEventKey


def update_human_fields(window, name, is_located_in, id):
    window[FieldEventKey.FIELD_HUMAN_NAME.value].Update(value=name)
    window[FieldEventKey.FIELD_HUMAN_LOCATION.value].Update(value=is_located_in)
    window[FieldEventKey.FIELD_CONNECTION_LEFT.value].Update(value=id)


def update_room_fields(window, name, type, id):
    window[FieldEventKey.FIELD_ROOM_NAME.value].Update(value=name)
    window[FieldEventKey.FIELD_ROOM_TYPE.value].Update(value=type)
    window[FieldEventKey.FIELD_CONNECTION_RIGHT.value].Update(value=id)


def update_device_fields(window, name, type, is_located_in, id):
    window[FieldEventKey.FIELD_DEVICE_NAME.value].Update(value=name)
    window[FieldEventKey.FIELD_DEVICE_TYPE.value].Update(value=type)
    window[FieldEventKey.FIELD_DEVICE_LOCATION.value].Update(value=is_located_in)
    window[FieldEventKey.FIELD_CONNECTION_RIGHT.value].Update(value=id)


def update_door_fields(window, name, is_open, is_door_of_a, is_door_of_b, id):
    window[FieldEventKey.FIELD_DOOR_NAME.value].Update(value=name)
    window[FieldEventKey.FIELD_DOOR_IS_OPEN.value].Update(value=is_open)
    window[FieldEventKey.FIELD_DOOR_IS_CLOSE.value].Update(value=is_open == False)
    window[FieldEventKey.FIELD_DOOR_ROOM_A.value].Update(value=is_door_of_a)
    window[FieldEventKey.FIELD_DOOR_ROOM_B.value].Update(value=is_door_of_b)
    window[FieldEventKey.FIELD_CONNECTION_RIGHT.value].Update(value=id)


def update_window_fields(window, name, is_open, is_window_of, id):
    window[FieldEventKey.FIELD_WINDOW_NAME.value].Update(value=name)
    window[FieldEventKey.FIELD_WINDOW_IS_OPEN.value].Update(value=is_open)
    window[FieldEventKey.FIELD_WINDOW_IS_CLOSE.value].Update(value=is_open == False)
    window[FieldEventKey.FIELD_WINDOW_ROOM.value].Update(value=is_window_of)
    window[FieldEventKey.FIELD_CONNECTION_RIGHT.value].Update(value=id)
