
grammar unclear_coverage;
//{<A,0.1>,<B,0.3>}
//Формула сокращённого языка логики высказываний
formula: OPENFIGURE subformula (COMMA subformula)* CLOSEFIGURE;
subformula: OPENBRACKET VAR COMMA DECIMAL CLOSEBRACKET;




//Lexer rules
DECIMAL: '0' | '1' | '0.' [0-9]+;
VAR: [A-Z]; //Буквы латинского языка для обозначения высказываний
COMMA: ','; //Отрицание
OPENBRACKET: '<'; //Открывающаяся скобка
CLOSEBRACKET: '>'; //Закрывающаяся скобка
OPENFIGURE: '{';
CLOSEFIGURE: '}';
