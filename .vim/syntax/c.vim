"===============================================================
" Highlight All Operators
"===============================================================
" C math operators
syn match cMathOperator display "[-+/*/%=]"
" C logical operators
syn match cLogicalOperator display "[!<>]=/="
syn match cLogicalOperator display "=="
" C pointer operators
syn match cPointerOperator display "->/|/."

hi cMathOperator          guifg=#3EFFE2
hi cBinaryOperator        guifg=#3EFFE2
hi cBinaryOperatorError   guifg=#3EFFE2
hi cLogicalOperator       guifg=#3EFFE2
hi cPointerOperator       guifg=#3EFFE2

"===============================================================
" Highlight All Functions
"===============================================================
syn match cFunction "/<[a-zA-Z_][a-zA-Z_0-9]*/>[^()]*)("me=e-2
syn match cFunction "/<[a-zA-Z_][a-zA-Z_0-9]*/>/s*("me=e-1

hi cFunction gui=None guifg=#B5A1FF

