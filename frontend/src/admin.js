let edit = document.getElementById('edit')
edit.onclick = function()
{
    let father = this.parentElement.parentElement.children

    document.getElementById('edit').style.display = 'none'
    document.getElementById('exclude').style.display = 'none'
    document.getElementById('Save').style.display = 'block'
    document.getElementById('Save').style.marginLeft = '30px'

    let array = []
    for(let cont = 1;cont<father.length - 1;cont++)
    {
        array[cont] = father[cont].innerHTML
    }

    for(let cont = 1;cont<father.length - 1;cont++)
    {
        let input = document.createElement('input')
        input.value = father[cont].innerHTML
        father[cont].innerHTML = ""
        father[cont].appendChild(input)
    }
}

let save = document.getElementById('Save')
save.onclick = function ()
{
    let father = this.parentElement.parentElement.children
    for(let cont = 1;cont<father.length - 1;cont++)
    {
        father[cont].innerHTML = father[cont].children[0].value
    }

    document.getElementById('edit').style.display = 'inline'
    document.getElementById('exclude').style.display = 'inline'
    document.getElementById('Save').style.display = 'none'
}

let exclude = document.getElementById('exclude')
exclude.onclick = function()
{
    let father = this.parentElement.parentElement
    father.remove()
}
