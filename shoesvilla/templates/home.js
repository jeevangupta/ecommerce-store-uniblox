
function ShowProducts(dom_id, product_count){

    let html = ``

    for (let i=1; i<=product_count; i++){
        html+=`
        <div class="card shadow text-center m-3 w-25 h-25">
            <div class="card-body">
                <h5 class="card-title mt-1">Shoe ${i}</h5>
                <div class="d-flex justify-content-center align-items-center mb-3">
                    <span class="icon"><i class="bi bi-card-image"></i></span>
                </div>
                <div class="d-flex justify-content-center align-items-center mb-3">
                    <span class="price"> ₹ 2000 </span>
                </div>
                
                <div class="">
                    <button type="button" class="add-cart btn btn-primary" id="s${i}" value=2000 title="Add to cart" data-toggle="tooltip">Add to cart</button>
                </div>
            </div>
        </div>
        `
    }

    $(`#${dom_id}`).html(html);

    $(`#${dom_id} .add-to-cart`).on('click', OnAddToCartClick);

    

}

function OnAddToCartClick(e){

}

function OnOpenCartClick(e){

    $(`#Cart`).modal('show')
    
}
