import pytest
from hamcrest import contains_string, greater_than, has_length

from superintendent.front import FrontHighLevelClient
from superintendent.matchers.commands import (
    contains_commands,
    contains_intent,
    is_event_list,
    is_text_suggest,
)


@pytest.fixture(scope='module')
def capabilities() -> str:
    return '7360292631805217937211'


@pytest.mark.parametrize('phrase', ['О чем тебя можно спросить?', 'Что ты умеешь?'])
def test_skill_list_skills(front: FrontHighLevelClient, phrase):
    # import pdb
    # pdb.set_trace()
    result = front.text(phrase)
    contains_intent(result, 'skill_list.skills')
    contains_commands(result,
                      is_text_suggest(callback_data=contains_string('"binding_type": "suggest"')),
                      is_event_list(items=has_length(greater_than(0))))
    result = front.text("А еще?")
    contains_intent(result, 'skill_list.anaphora')
    contains_commands(result,
                      is_text_suggest(callback_data=contains_string('"binding_type": "suggest"')),
                      is_event_list(items=has_length(greater_than(0))))









import pytest
from hamcrest import has_entries, contains_string

from superintendent.front import FrontHighLevelClient
from superintendent.matchers.commands import contains_commands, contains_intent
from superintendent.matchers.commands.commands import is_media, is_text_suggest, is_text

pytestmark = pytest.mark.user_index(index=2)


@pytest.fixture(scope='module')
def capabilities() -> str:
    return '633825300112313260894165400639'


def test_podcast_discover_scroll_themes(auth_front: FrontHighLevelClient):
    # import pdb
    # pdb.set_trace()
    result = auth_front.text("какие подкасты у тебя есть?")
    contains_commands(result, is_text_suggest(callback_data=contains_string('"binding_type": "suggest"')),
                      is_text(text=contains_string('Могу предложить подкасты')))
    contains_intent(result, 'podcasts_v2.discover')
    result = auth_front.text("Ещё")
    contains_commands(result, is_text_suggest(callback_data=contains_string('"binding_type": "suggest"')),
                      is_text(text=contains_string('Могу предложить подкасты')))
    contains_intent(result, 'podcasts_v2.podcasts_v2_fsm_routine')


def test_podcast_discover_choice_themes(auth_front: FrontHighLevelClient):
    # import pdb
    # pdb.set_trace()
    result = auth_front.text("какие подкасты у тебя есть?")
    choice_suggest = result['commands'][1]['text']
    result = auth_front.text(choice_suggest)
    contains_commands(result, is_media(commands=has_entries(media_type="podcast", skill_name="podcasts_v2")))
    contains_intent(result, 'podcasts_v2.podcasts_v2_fsm_routine')

def test_podcast_search_thematic(auth_front: FrontHighLevelClient):
    # import pdb
    # pdb.set_trace()
    result = auth_front.text("включи подкаст про спорт")
    contains_intent(result, 'podcasts_v2.search_thematic')
    contains_commands(result,
                      is_text_suggest(callback_data=contains_string('"binding_type": "suggest"')),
                      is_text(text=contains_string('Вот какие подкасты у меня есть')))
    choice_suggest = result['commands'][1]['text']
    result = auth_front.text(choice_suggest)
    contains_intent(result, 'podcasts_v2.search_thematic')


def test_podcast_search_thematic_scroll_thematic(auth_front: FrontHighLevelClient):
    # import pdb
    # pdb.set_trace()
    result = auth_front.text("включи подкаст про спорт")
    contains_intent(result, 'podcasts_v2.search_thematic')
    result = auth_front.text("еще")
    contains_intent(result, 'podcasts_v2.')
    result = auth_front.text("не знаю")
    contains_intent(result, 'podcasts_v2.')


def test_podcast_random(auth_front: FrontHighLevelClient):
    result = auth_front.text("включи подкаст про спорт")
    contains_intent(result, 'podcasts_v2.random')
    result = auth_front.text("включить другой эпизод")

    result = auth_front.text("включить другой подкаст")