import React from 'react'
import PropTypes from 'prop-types'

const Details = ({ details }) => (
  <ul>
    {
      details.map((detail, i) => {
        let text = detail[0] + ': ' + detail[1]
        return <li key={i}>{text}</li>
      })
    }
  </ul>
)

Details.PropTypes = {
  posts: PropTypes.array.isRequired
}

export default Details