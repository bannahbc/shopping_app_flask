

const pFrom = document.getElementById('productForm')
const aDP = document.getElementById('addProductBtn')
const closeBtn = document.getElementById('closeBtn')
const productForm = document.getElementById('product-form')
closeBtn.addEventListener('click',()=>{
    pFrom.style.display = 'none'
    productForm.reset();
})
aDP? aDP.addEventListener('click',()=>{
    pFrom.style.display = 'flex'
}):''



$('#product-form').on('submit', function(e) {
    e.preventDefault(); // Prevents the default form submission
    let formData = new FormData(this)
    $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: formData,
        processData: false, // Prevents jQuery from processing the data
        contentType: false, // Prevents jQuery from setting the content type // Serialize form data
        // data: $(this).serialize(), // Serialize form data
        success: function(response) {
            Swal.fire({
                position: "center",
                icon: "success",
                title: response.message,
                showConfirmButton: false,
                timer: 1900
              });// Show success message
        },
        error: function(xhr) {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: xhr.responseJSON.error ?xhr.responseJSON.error:"Something went wrong!",
             
              });
        }
    });
});
const cateBtn = document.getElementById('cateBtn')
const cateName = document.getElementById('cateName')
cateBtn.addEventListener('click',(e)=>{
    e.preventDefault();

    $.ajax({
        type:'POST',
        url:'/admin/createCategory',
        contentType:'application/json',
        data:JSON.stringify({
            categoryName:cateName.value
        }),
        success:function(res){
            Swal.fire({
                position: "center",
                icon: "success",
                title: res.message,
                showConfirmButton: false,
                timer: 1900
              }).then((result)=>{

                  window.location.reload()
              })
        },error:function(xhr){
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: xhr.responseJSON.message ?xhr.responseJSON.message:"Something went wrong!",
             
              });

        }
    })
})

// Swal.fire({
//     position: "top-end",
//     icon: "success",
//     title: "Your work has been saved",
//     showConfirmButton: false,
//     timer: 1500
//   });


// Swal.fire({
//     icon: "error",
//     title: "Oops...",
//     text: "Something went wrong!",
//     footer: '<a href="#">Why do I have this issue?</a>'
//   });