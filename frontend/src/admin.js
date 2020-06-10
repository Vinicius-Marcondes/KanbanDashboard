let refresh = document.getElementById('refresh')
let tbody = document.querySelector('tbody')

function loadUsers()
{
    fetch('https://reqres.in/api/users?page=2')
        .then(function(response) {
            return response.json()
        })
        .then(function(response) {
            response.data.forEach(function (user) {

                let id = document.createElement('td')
                id.innerHTML = user.id

                let firstName = document.createElement('td')
                firstName.innerHTML = user.first_name

                let email = document.createElement('td')
                email.innerHTML = user.email

                let title = document.createElement('td')
                title.innerHTML = 'titulo'

                let oloko = document.createElement('td')
                oloko.innerHTML = 'oloko'

                //Edit

                let tdbutton = document.createElement('td')

                let edit = document.createElement('button')
                edit.classList.add("edit")
                edit.setAttribute("id",`edit${user.id}`)
                edit.setAttribute("onclick",`editUser(edit${user.id})`)

                let img = document.createElement('img')
                img.classList.add("img")
                img.setAttribute("src","images/icons/edit.png")

                tdbutton.appendChild(edit)
                edit.appendChild(img)

                //Exclude

                let exclude = document.createElement('button')
                exclude.classList.add("exclude")
                exclude.setAttribute("id",`exclude${user.id}`)
                exclude.setAttribute("onclick",`deleteUser(exclude${user.id})`)

                let img2 = document.createElement('img')
                img2.classList.add("img")
                img2.setAttribute("src","images/icons/delete.png")

                tdbutton.appendChild(exclude)
                exclude.appendChild(img2)

                //Save

                let save = document.createElement('button')
                save.classList.add("Save")
                save.setAttribute("id",`save${user.id}`)
                save.setAttribute("onclick",`saveUser(save${user.id})`)

                let img3 = document.createElement('img')
                img3.classList.add("img")
                img3.setAttribute("src","images/icons/save.png")

                tdbutton.appendChild(save)
                save.appendChild(img3)

                let tr = document.createElement('tr')

                tbody.appendChild(tr)
                tr.appendChild(id)
                tr.appendChild(firstName)
                tr.appendChild(email)
                tr.appendChild(title)
                tr.appendChild(oloko)
                tr.appendChild(tdbutton)
            })
        })
}

function editUser(id)
{
    let father = id.parentElement.parentElement.children

    id.style.display = 'none'
    id.nextElementSibling.style.display = 'none'
    id.nextElementSibling.nextElementSibling.style.display = 'inline'

    for(let cont = 1;cont<father.length - 1;cont++)
    {
        let input = document.createElement('input')
        input.value = father[cont].innerHTML
        father[cont].innerHTML = ""
        father[cont].appendChild(input)
    }

}

function saveUser(id)
{
    let father = id.parentElement.parentElement.children

    id.previousElementSibling.style.display = 'inline'
    id.previousElementSibling.previousElementSibling.style.display = 'inline'
    id.style.display = 'none'

    for(let cont = 1;cont<father.length - 1;cont++)
    {
        father[cont].innerHTML = father[cont].children[0].value
    }

}

function deleteUser(id)
{
    let father = id.parentElement.parentElement
    father.remove()
}