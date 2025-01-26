import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductOrderPage = () => {
  const [products, setProducts] = useState([]);
  const [orders, setOrders] = useState({});
  const [loading, setLoading] = useState(true);
  const [orderID, setorderID] = useState(1);
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const token = localStorage.getItem('accessToken');
        const response = await axios.get('http://127.0.0.1:8000/api/products/', {
          // headers: { Authorization: `Bearer ${token}` }
        });
        setProducts(response.data);
        var aanqezi =  await axios.post('http://127.0.0.1:8000/api/orders/', 
          { total_cost: 0 }, 
          // { headers: { Authorization: `Bearer ${token}` } }
        );
        setorderID(aanqezi.data.id);
        setLoading(false);
      } catch (error) {
        console.error('Failed to fetch products', error);
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  const createOrder = async (productId) => {
      const quantity = (orders[productId] || 0) + 1;
  };

  const submitOrder = async (productId) => {
    try {
      const token = localStorage.getItem('accessToken');
      const quantity = (orders[productId] || 0);
      await axios.post('http://127.0.0.1:8000/api/order_detail/', 
        { product_id: productId, quantity:quantity}, 
      );
      setOrders(prev => ({
        ...prev,
        [productId]: quantity
      }));
    } catch (error) {
      console.error('Failed to create order', error);
    }
  };

  if (loading) return <div>Loading products...</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Products</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {products.map(product => (
          <div 
            key={product.id} 
            className="border p-4 rounded shadow-md"
          >
            <h2 className="text-xl font-semibold">{product.name}</h2>
            <p className="text-gray-600">Brand: {product.brand}</p>
            <p className="text-lg font-bold">${product.price}</p>
            <div className="flex items-center mt-2">
              <button 
                onClick={() => createOrder(product.id)}
                className="bg-blue-500 text-white px-4 py-2 rounded"
              >
                Order
              </button>
              <button 
                onClick={() => submitOrder(product.id)}
                className="bg-blue-500 text-white px-4 py-2 rounded"
              >
                Submit
              </button>
              {orders[product.id] && (
                <span className="ml-4 text-gray-700">
                  Ordered: {orders[product.id]}
                </span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProductOrderPage;