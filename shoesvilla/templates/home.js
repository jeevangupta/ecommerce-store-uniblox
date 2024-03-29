
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
let discount_code = ""

function OnAddToCartClick(e){
    let user_id = $(`#user-id`).val()
    let product_id = $(this).attr("id")
    let product_price = $(this).attr("price")
    let product_name = $(this).attr("name")

    let payload = {"user_id":user_id, "id":product_id, "name":product_name, "price":product_price}

    $(`#spinner`).show()
    response = postData(payload,"/shoesvilla/add-to-cart/");

    response.then(function(data){
        let status = data["status"]
        let mssg = data["mssg"]

        product_store = data["product_store"]
        
        if (status){
            window.alert("Product "+ product_name + " added in Cart");
        }
        else{
            window.alert(mssg);
        }

        console.log(status);
        console.log(mssg);

        $(`#spinner`).hide()
    })

}

function GetDiscountCode(){
    let user_id = $(`#user-id`).val();
    let payload = {"user_id":user_id}
    let codes = {}
    let response = postData(payload,"/shoesvilla/get-discount-code/");

    response.then(function(data){
        let status = data["status"]
        //let mssg = data["mssg"]
        let html = ``

        if (status){
            let codes = data["discount_details"]
            discount_code = codes.discount_code
            html = `
                <span class="mt-2"> Applicable Discount: ${codes.discount} </span>
            `
        }
        else{
            html = `
                <span class="mt-2"> Applicable Discount: No Item in Cart </span>
            `
        }

        $("#discount-dt").html(html);
    })
}

function OnOpenCartClick(e){
    let totalPrice = 0;
    let user_id = $(`#user-id`).val();

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
    let products = {}
    if (user_id in product_store){
        products = product_store[user_id]
    }

    Object.keys(products).forEach(productId => {
        let product = products[productId];
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
    </table>
    `

    $("#cart-items").html(html_table);

    $(`#Cart`).modal('show')

    GetDiscountCode()
    
}


function OnCheckoutClick(e){
    let user_id = $(`#user-id`).val();

    let payload = {"user_id":user_id, "discount_code":discount_code}

    response = postData(payload,"/shoesvilla/checkout/");

    $(`#spinner`).show()

    response.then(function(data){
        $(`#Cart`).modal('hide')
        let status = data["status"]
        let mssg = data["mssg"]
        
        if (status){
            //reset 
            product_store = {}
            discount_details = {}

            $("#cart-items").html("No Item in the cart");
        }
        window.alert(mssg);

        console.log(mssg);
        $(`#spinner`).hide()
    })

}
