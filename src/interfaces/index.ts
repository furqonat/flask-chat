interface IResponse {
    user: {
        uid: string,
        name: string,
        is_active: boolean
    },
    chat: [

    ]
}

export { IResponse }