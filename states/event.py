from aiogram.dispatcher.filters.state import State, StatesGroup


class EventStates(StatesGroup):
    normal = State()
    waiting_for_name = State()
    waiting_for_description = State()
    waiting_for_day = State()
    waiting_for_time = State()

    leave_group = State()
    manage_own_group = State()

    event_edit = State()
