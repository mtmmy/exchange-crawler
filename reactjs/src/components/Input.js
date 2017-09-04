import React from 'react'
import PropTypes from 'prop-types'

const InputStockId = ({ value, onChange, onClick }) => (
  <div>
    Stock ID: <input onChange={e => onChange(e.target.value)} value={value} />
  </div>
)

InputStockId.propTypes = {
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired
}

export default InputStockId