import fetch from 'isomorphic-fetch'

export const CHANGE_STOCK = 'CHANGE_STOCK'
export const REQUEST_STOCK = 'REQUEST_STOCK'
export const RECEIVE_STOCK = 'RECEIVE_STOCK'

export const changedStock = stock => ({
    type: CHANGE_STOCK,
    stock
})

export const requestStock = stock => ({
    type: REQUEST_STOCK,
    stock
})

export const receiveStock = (stock, json) => ({
    type: RECEIVE_STOCK,
    stock,
    details: Object.entries(json.StockInfo),
    receivedAt: Date.now()
})

const fetchPosts = stock => dispatch => {
    dispatch(requestStock(stock))
    
    let proxyUrl = 'https://cors-anywhere.herokuapp.com/'
    let targetUrl = `https://www.cmoney.tw/follow/channel/getdata/GetStockOtherInfo?stockId=${stock}&channelId=335735&_=1504450326542`

    return fetch(proxyUrl + targetUrl)
    .then(response => response.json())
        .then(json => dispatch(receiveStock(stock, json)))
}

export const fetchStockIfNeeded = stock => (dispatch, getState) => {
    return dispatch(fetchPosts(stock))
}
