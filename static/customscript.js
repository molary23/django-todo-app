const replicate_todo = (todo) => {
    let ask = confirm('Are you sure you want to create a new Todo that is similar to this one?')

    if (!ask) {
        return null
    }


    const name = document.getElementById('name'),
        priority = document.getElementById('priority'),
        description = document.getElementById('description'),
        modal = document.getElementById('myModal')

    name.value = (todo[0])
    priority.value = (todo[1])
    description.value = (todo[2])

    modal.style.display = 'block'


}

const edit_todo = (todo) => {
    const form = document.getElementById('todo_form'),
        name = document.getElementById('name'),
        priority = document.getElementById('priority'),
        description = document.getElementById('description'),
        modal = document.getElementById('myModal')

    name.value = (todo[0])
    priority.value = (todo[1])
    description.value = (todo[2])

    form.method = 'post'
    form.action = `${todo[3]}/edit/`

    modal.style.display = 'block'
}

const delete_todo = (id) => {
    return confirm('Are you sure you want to create a new Todo that is similar to this one?')

}
const closeModal = () => {
    const modal = document.getElementById('myModal')
    modal.style.display = 'none'
}