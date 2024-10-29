from automata.pda.npda import NPDA


def q3a() -> NPDA:
    return NPDA(
        states={1, 2, 3, 4},
        input_symbols={'a', 'b'},
        stack_symbols={'$', 'x'},
        initial_state=1,
        final_states={4},
        initial_stack_symbol='$',
        acceptance_mode='final_state',
        transitions={
            1: {
                'a': {
                    'x': {(1, ('x', 'x'))},
                    '$': {(1, ('x', '$'))}
                },
                'b': {
                    'x': {(1, ('x', 'x'))},
                    '$': {(1, ('x', '$'))}
                },
                '': {
                    'x': {(2, 'x')}
                }
            },
            2: {
                'a': {
                    'x': {(2, '')}
                },
                'b': {
                    'x': {(3, '')}
                }
            },
            3: {
                'a': {
                    'x': {(3, '')}
                },
                'b': {
                    'x': {(3, '')}
                },
                '': {
                    '$': {(4, '')}
                }
            }
        }
    )


def q3b():
    return [
        ('S', ['aSa', 'aAb', 'bSa', 'bAb']),
        ('A', ['aAa', 'aAb', 'bAb', 'bAa', ''])
    ]
