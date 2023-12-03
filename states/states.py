from aiogram.dispatcher.filters.state import State, StatesGroup


class horo_states():
    zod = []
    message_to_del = []


class anek_state():
    id_a = []


class compitability:
    znak_w = []
    znak_m = []


class WaitToCall(StatesGroup):
    callhandlerstate = State()


class CityGameState(StatesGroup):
    citygamestate = State()
    bottyrn = State()




class Bomber(StatesGroup):
    bomb = State()


class ID(StatesGroup):
    id = State()
