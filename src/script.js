// $(document).ready(function () {
//
//     $('.carousel').owlCarousel({
//         margin:30,
//         loop:true,
//         zIndex:999,
//
//         autoplayTimeOut:100,
//         autoplayHoverPauser:true,
//         responsive:{
//             0:{
//                 items:1,
//                 nav:false
//             },
//             800:{
//                 items:2,
//                 nav:false
//             },
//             3000:{
//                 items:3,
//                 nav:false
//             }
//         }
//     });
// });
const btnMobile = document.getElementById('btn-mobile');
function toggleMenu(){
    const nav = document.getElementById('nav');
    nav.classList.toggle('active');

}
btnMobile.addEventListener('click',toggleMenu);
