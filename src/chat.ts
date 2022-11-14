import { io } from 'socket.io-client'
import './index.css'
import { IResponse } from './interfaces'

const socket = io('http://localhost:5000')

let user = {}

socket.on('connect', () => {
    console.log('connected', "halo")
})

socket.on('message', (data) => {
    console.log(data)
})

const userChat = new Proxy(user, {
    set: (target: any, key, value) => {
        target[key] = value
        return true
    }
})
socket.on('join', (data: IResponse) => {
    userChat.user = data.user
    
})

// proxy when user join set user

class ChatList extends HTMLElement {
    joinRoom(roomId?: string) {
        socket.emit('join', { roomId: roomId })
    }

    connectedCallback() {
        const hasRoomId = this.hasAttribute('room-id')
        const dataTitle = this.getAttribute('data-title')
        const dataStatus = this.getAttribute('data-status')
        const div = document.createElement('div')
        this.addEventListener('click', () => {
            const roomId = this.getAttribute('room-id')
            if (hasRoomId) {
                this.joinRoom(roomId?.toString())
            }
        })
        div.classList.add('chat-item')
        const title = document.createElement('h3')
        title.classList.add('chat-title')
        title.textContent = dataTitle
        const status = document.createElement('p')
        status.classList.add('chat-status')
        status.textContent = dataStatus === "True" ? "Online" : "Offline"
        div.appendChild(title)
        div.appendChild(status)
        this.appendChild(div)
    }
}
class ChatItem extends HTMLElement {

    connectedCallback() {
        const header = document.createElement('header')
        if (user) {
            header.textContent = userChat.user.name
        }
        this.appendChild(header)
    }
}

customElements.define('chat-list', ChatList)
customElements.define('chat-item', ChatItem)

export { socket, ChatList as ChatItem }