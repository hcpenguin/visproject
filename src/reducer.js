export const defaultState = {
    "currentYear": "2000",
    "currentViolation": "MURDER & NON NEGL. MANSLAUGHTER",
}

export const reducer = (state = defaultState, action) => {
    const actionToState = {
        'UPDATE_YEAR': {...state, currentYear: action.currentYear},
        'UPDATE_VIOLATION': {...state, currentViolation: action.currentViolation},
    };

    return actionToState[action.type] || state;
}
