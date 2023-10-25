const btnCart = document.querySelector('.container-cart-icon');
const containerCartProducts = document.querySelector('.container-cart-products');

btnCart.addEventListener('click', () => {
    containerCartProducts.classList.toggle('hidden-cart');
});

const cartInfo = document.querySelector('.cart-product');
const rowProduct = document.querySelector('.row-product');

const prodcuctList = document.querySelector('.filters-content');
//Lista para todos los productos 
let allproducts = [];

let valorTotal = document.querySelector('.total-pagar');
const countProducts = document.querySelector('#contador-productos');



prodcuctList.addEventListener('click', e => {
    if (e.target.classList.contains('btn-add-cart')) {
        const product = e.target.parentElement;

        const infoProduct = {
            quantity: 1,
            title: product.querySelector('h5').textContent,
            price: product.querySelector('h6').textContent,
        };
        
        const exist = allproducts.some(product => product.title === infoProduct.title)
        
        if (exist){
            const products = allproducts.map(product =>{
                if (product.title === infoProduct.title){
                    product.quantity++;
                    return product;
                }else {
                    return product;
                }
            });
            allproducts = [...products];
        } else{ 
            
            allproducts = [...allproducts, infoProduct];
        }


        
        showHTML();     
    }
       console.log(allproducts)
});

rowProduct.addEventListener('click', e => {
	if (e.target.classList.contains('icon-close')) {
		const product = e.target.parentElement;
		const title = product.querySelector('p').textContent;

		allproducts = allproducts.filter(
			product => product.title !== title
		);

		console.log(allproducts);

		showHTML();
	}
});

const showHTML = () => {
    
    if(!allproducts.length){
        containerCartProducts.innerHTML=`
        <p class="cart-empty">El carrito está vacío</p>
        `
    };
    
    
    
    //limpiar 
    rowProduct.innerHTML='';

    let total = 0;
    let totalProducts = 0;

    allproducts.forEach(product => {
        const containerProduct = document.createElement('div');
        containerProduct.classList.add('cart-product');

        containerProduct.innerHTML = ` 
                <div class="info-cart-product">
                <span class="cantidad-producto-carrito">${product.quantity}</span>
                <p class="titulo-producto-carrito">${product.title}</p>
                <span class="precio-producto-carrito">${product.price}</span>
                </div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="icon-close">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
                    `;

        rowProduct.append(containerProduct);
        
        total =
         total + parseInt(product.quantity * product.price.slice(1));
        totalProducts = totalProducts + product.quantity; 
    });

    valorTotal.innerText = `$${total}`;
    countProducts.innerText = totalProducts;
    console.log(totalProducts)
};