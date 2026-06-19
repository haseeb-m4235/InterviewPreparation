from langgraph.graph import StateGraph, Start, End
from interviewer_agent.nodes import human_node, asker, question_creator, evaluator, questions_ender, question_list_check
from interviewer_agent.models import InterviewerState, Context
from langgraph.store.memory import InMemoryStore
from langgraph.checkpoint.memory import InMemorySaver

BUILDER = StateGraph(state_schema=InterviewerState, context_schema=Context)

BUILDER.add_node('Human', human_node)
BUILDER.add_node('Asker', asker)
BUILDER.add_node('QuestionCreator', question_creator)
BUILDER.add_node('Evaluator', evaluator)

BUILDER.add_edge(Start, 'Human')
BUILDER.add_conditional_edge('Human', question_list_check, {"QuestionCreator": "QuestionCreator", "Asker": "Asker"})
BUILDER.add_edge('QuestionCreator', 'Asker')
BUILDER.add_conditional_edge('Asker', questions_ender, {"Human": "Human", "Evaluator": "Evaluator"})
BUILDER.add_edge("Evaluator", End)

def compile_interviewer_agent_graph() -> StateGraph:
    store = InMemoryStore()
    checkpointer = InMemorySaver()
    return BUILDER.compile(store=store, checkpointer=checkpointer)