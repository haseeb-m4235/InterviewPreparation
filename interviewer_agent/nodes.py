from interviewer_agent.models import InterviewerState
from prompts import question_creation_prompt, evaluation_prompt
from langgraph.runtime import Runtime
from models import Context
from ollama import chat


def human_node(state: InterviewerState, runtime: Runtime[Context]) -> str:
    if not state['job_description']:
        # Interrupt and ask for job description
        # update job descritpion in state
        # next node is Questions_creator
        pass
    else:
        # Interrupt with the current question, append answer to answers_list, and next node is asker
        pass

def question_creator(state: InterviewerState, runtime: Runtime[Context]) -> str:
    # Get the job description
    # Prepare prompt for question creation
    prompt = question_creation_prompt.format(job_description=state['job_description'])
    # Call LLM to generate questions based on the job description
    response = chat(
    model='runtime.model_name', 
    messages=[
        {'role': 'system', 'content': 'prompt'}
    ]
)
    # Extract questions
    # Update questions_list in state
    # Next node is asker
    pass

def question_list_check(state: InterviewerState, runtime: Runtime[Context]) -> str:
    # Check if question list is generated or not
    if not state['questions_list']:
        return 'QuestionCreator'
    else:
        return 'Asker'

def asker(state: InterviewerState, runtime: Runtime[Context]) -> str:
    # update the state's current question, increment current_index in state
    # next node is questions_ender
    state['current_question'] = state['questions_list'][state['current_index']]
    state['current_index'] += 1

def questions_ender(state: InterviewerState, runtime: Runtime[Context]) -> str:
    # Check if current_index in state is less than length of questions list
    # Yes: next node is human_node
    # No: next node is evaluator
    if state['current_index'] < len(state['questions_list']):
        return 'Human'
    else:
        return 'Evaluator'

def evaluator(state: InterviewerState, runtime: Runtime[Context]) -> str:
    # Get Questions list and answers list from state
    # Prepare prompt for evaluation
    # call llm to generate report
    # Extract report
    # Update evaluation_report in state
    pass