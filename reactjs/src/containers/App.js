import React from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { changedStock, fetchStockIfNeeded } from '../actions'
import InputStockId from '../components/Input'
import Details from '../components/Details'

class App extends React.Component {
  static propTypes = {
    changedStock: PropTypes.string.isRequired,
    dispatch: PropTypes.func.isRequired
  }

  componentDidMount() {
    const { dispatch, changedStock } = this.props
    dispatch(fetchStockIfNeeded(changedStock))
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.changedStock !== this.props.changedStock){
      const { dispatch, changedStock } = nextProps
      dispatch(fetchStockIfNeeded(changedStock))
    }
  }

  handleChange = stock => {
    this.props.dispatch(changedStock(stock))
  }

  handleClick = e => {
    e.preventDefault()

    const { dispatch, changedStock } = this.props
    dispatch(fetchStockIfNeeded(changedStock))
  }

  render() {
    const { changedStock, details, isFetching } = this.props
    console.log(details)    
    return (
      <div>
        <InputStockId onChange={this.handleChange} value={changedStock} />
        <button onClick={this.handleClick}>Send</button>
        {details ? <Details details={details} /> : <h2>Loading...</h2>}        
      </div>
    )
  }
}

const mapStateToProps = state => {
  const {changedStock, detailsOfStock, isFetching} = state
  // console.log('====================state=====================')
  // console.log(state)
  const {
    details: details
  } = detailsOfStock || {
    isFetching: true,
    details: {}
  }

  return {
    changedStock,
    isFetching,
    details
  }
}

export default connect(mapStateToProps)(App)
