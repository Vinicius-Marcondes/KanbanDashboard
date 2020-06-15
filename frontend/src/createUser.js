//Inputs effects
document.querySelectorAll('.inputs input').forEach(function(e)
{
    e.onfocus = function ()
    {
        if(e.value === e.name)
        {
            if (e.name === 'Password')
            {
                e.value = '';
                e.type = 'Password'
            }
            e.value = ''
        }
    }

    e.onblur = function ()
    {
        if(e.value === '')
        {
            e.value = e.name
            e.type = 'Text'
        }
    }
})

//Upload Image User
function file_changed()
{
    let selectedFile = document.querySelector('.imageUser input').files[0]
    let img = document.querySelector('.imageUser img')

    let reader = new FileReader()
    reader.onload = function()
    {
        img.src = this.result
    }
    reader.readAsDataURL(selectedFile)
    img.style.clipPath =  'circle(50% at 50% 50%)'
}
