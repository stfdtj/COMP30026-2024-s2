from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


def q1a():
    return DFA(states={1, 2, 3, 4, 5, 6, 7}, input_symbols={'0', '1'}, transitions={
        1: {'0': 2, '1': 1},
        2: {'0': 3, '1': 1},
        3: {'0': 2, '1': 4},
        4: {'1': 4, '0': 5},
        5: {'0': 6, '1': 4},
        6: {'0': 5, '1': 7},
        7: {'0': 7, '1': 7}
    },
        initial_state=1,
        final_states={6, 7}
    )


def q1b():
    return '((0|1)*1)*00(00)*1((0|1)*1)*00(00)*(1(0|1)*)*'
