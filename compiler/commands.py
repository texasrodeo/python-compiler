from compiler.parser import PythonLexer

commands = {
    '+':        'ADD',
    '-':        'SUB',
    '/':        'DIV',
    '*':        'MUL',
    'and':      'AND',
    'or':       'OR',
    'not':      'NOT',
    'True':     True,
    'False':    False,
    '==':       'ISEQ',
    '>':        'ISGT',
    '>=':       'ISGE',
    'push':     'PUSH',
    'load':     'LOAD',
    'store':    'STORE',
    'halt':     'HALT'
}