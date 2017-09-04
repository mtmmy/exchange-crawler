import { combineReducers } from 'redux'
import { CHANGE_STOCK, REQUEST_STOCK, RECEIVE_STOCK } from '../actions'

const changedStock = (state = '6180', action) => {
  switch (action.type) {
    case CHANGE_STOCK:
      return action.stock
    default:
      return state
  }
}

const detailsOfStock = (state = {}, action) => {
  switch (action.type) {
    case REQUEST_STOCK:
      return {
        ...state,
        isFetching: true
      }
    case RECEIVE_STOCK:    
      return {
        ...state,
        isFetching: false,
        details: action.details
      }
    default:
      return state
  }
}

const rootReducer = combineReducers({
  detailsOfStock,
  changedStock
})

export default rootReducer