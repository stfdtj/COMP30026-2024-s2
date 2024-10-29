from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


def q2a() -> str:
    return '0'


def rename_dfa(dfa: DFA, prefix) -> DFA:
    return DFA(
        states={(prefix, q) for q in dfa.states},
        final_states={(prefix, q) for q in dfa.final_states},
        initial_state=(prefix, dfa.initial_state),
        input_symbols=dfa.input_symbols,
        transitions={
            (prefix, qa): {
                sym: (prefix, qb) for sym, qb in t.items()
            } for qa, t in dfa.transitions.items()
        }
    )


def thaw_transitions_dfa(transitions):
    return {q1: {a: {q2} for a, q2 in t.items()}
            for q1, t in transitions.items()}


def q2b(a: DFA, b: DFA) -> NFA:
    aorig = a.to_complete()
    a = rename_dfa(aorig, 'A')
    b = b.to_complete()
    c = rename_dfa(aorig, 'C')
    states = set(a.states | c.states)
    transitions = thaw_transitions_dfa(
        a.transitions) | thaw_transitions_dfa(c.transitions)
    for i, qa in enumerate(aorig.states):
        b2 = rename_dfa(b, i)
        states |= b2.states
        transitions |= thaw_transitions_dfa(b2.transitions)
        transitions[('A', qa)].setdefault('', set()).add(b2.initial_state)
        for qb in b2.final_states:
            transitions[qb].setdefault('', set()).add(('C', qa))
    return NFA(
        states=states,
        input_symbols=a.input_symbols | b.input_symbols,
        transitions=transitions,
        initial_state=a.initial_state,
        final_states=c.final_states
    )
