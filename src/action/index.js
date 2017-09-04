export const REQUEST_STOCK = 'REQUEST_STOCK'

export const requestStock = stock => {
    type: REQUEST_STOCK,
        stock
}

export const receiveStock = (stock, json) => ({
    type: RECEIVE_POSTS,
    stock,
    posts: json.data.children.map(child => child.data),
    receivedAt: Date.now()
})

const fetchPosts = stock => dispatch => {
    dispatch(requestPosts(stock))
    return fetch(`http://www.cmoney.tw/follow/channel/getdata/GetStockOtherInfo?stockId=${stock}&channelId=104139&_=1504450326542`)
        .then(response => response.json())
        .then(json => dispatch(receiveStock(stock, json)))
}
