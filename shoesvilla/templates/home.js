
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
                    <button type="button" class="add-to-cart btn btn-primary" id="sku${i}" price=2000 name="Shoe ${i}"
                    title="Add to cart" data-toggle="tooltip">Add to cart</button>
                </div>
            </div>
        </div>
        `
    }

    $(`#${dom_id}`).html(html);

    $(`#${dom_id} .add-to-cart`).on('click', OnAddToCartClick);

    

}

let product_store = {}

function OnAddToCartClick(e){

    let product_id = $(this).attr("id")
    let product_price = $(this).attr("price")
    let product_name = $(this).attr("name")

    let payload = {"id":product_id,"name":product_name,"price":product_price}

    response = postData(payload,"/shoesvilla/add-to-cart/");

    response.then(function(data){
        let status = data["status"]
        product_store = data["product_store"]

        if (status){
            window.alert("Item add in Cart");
        }
        console.log(status);
    })

}

function OnOpenCartClick(e){
    let totalPrice = 0;

    let html_table = `<table class="table">
    <thead>
      <tr>
        <th scope="col">ID</th>
        <th scope="col">NAME</th>
        <th scope="col">PRICE</th>
      </tr>
    </thead>
    
    <tbody>`

    // Loop over each product in the product_store object
    Object.keys(product_store).forEach(productId => {
        let product = product_store[productId];
        html_table += `
        <tr>
            <th scope="row">${productId}</th>
            <td>${product.name}</td>
            <td>₹${product.price}</td>
        </tr>
        `
        totalPrice += parseFloat(product.price);
    });

    html_table += `
        </tbody>
        <tfoot>
        <tr>
            <th colspan="2" class="text-right">Grand Total:</th>
                <td>₹${totalPrice.toFixed(2)}</td>
            </tr>
        </tfoot>
    </table>`

    $("#cart-items").html(html_table);
    $(`#Cart`).modal('show')
    
}
