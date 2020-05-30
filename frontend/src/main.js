//Create all variants
let emailId = document.getElementById('Email')
let passId = document.getElementById('Password')
let enterButton = document.getElementById('enter')

//Effects Login Page
emailId.onfocus = function() {this.value = ''}
emailId.onblur = function() {this.value = this.id}
passId.onfocus = function() {this.value = ''; this.type = 'Password'}
passId.onblur = function() {if(this.value === "") {this.value = this.id; this.type = 'Text'}}





