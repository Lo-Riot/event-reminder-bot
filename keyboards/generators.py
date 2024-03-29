from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db.models import Group


def get_groups_kb(groups: list[Group]) -> InlineKeyboardMarkup:
    """ Generates keyboard from groups """
    groups_kb = InlineKeyboardMarkup()

    for group in groups:
        groups_kb.add(InlineKeyboardButton(
            group.name, callback_data=str(group.id)
        ))
    return groups_kb


def get_switchable_kb(
    entities: list, row_width=4, done_button_text="Done"
) -> InlineKeyboardMarkup:

    """ Generates keyboard from db entities """
    entities_kb = InlineKeyboardMarkup(row_width)

    for entity in entities:
        entities_kb.insert(
            InlineKeyboardButton(entity.name, callback_data=entity.id)
        )
    entities_kb.row(InlineKeyboardButton(
        done_button_text, callback_data="done"
    ))

    return entities_kb
