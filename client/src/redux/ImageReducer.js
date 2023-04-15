
const defaultState = {
    image: ''
}

const imageReducer = (state=defaultState, action) => {
    switch (action.type) {
        case 'UPDATE_IMAGE':
            return {...state, image: action.payload}
        default:
            return state
    }
}

export default imageReducer