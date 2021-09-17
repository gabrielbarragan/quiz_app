console.log('Hello quiz data view')

const url = window.location.href
console.log(url)

$.ajax({
    type:'GET',
    url:`${url}`,
    success: function(response){
        console.log(response)
    },
    error:function(error){
        console.log(error)
    }
})
