Hàm Sigmoid dược áp dụng dộc lập trên từng phần tử của $x_{l}$ là:
$$
\sigma( x_{l} )={\frac{1} {1+e^{-x_{l}}}}. \tag{2.2}
$$
Hàm Softmax cho $x_{l}$ cho từng vị trí $( i, j )$ trong bản dồ dặc trưng $x_{l}$ dược
viết nhu sau:
$$
\mathrm{S o f t m a x} ( x_{l} )_{i, j, k}={\frac{e^{x_{l, i, j, k}}} {\sum_{k^{\prime}=1}^{c} e^{x_{l, i, j, k^{\prime}}}}} \tag{2.3}
$$
trong dó,
 $x_{l, i, j, k}$ là giá trị tại vị trí $( i, j )$ và kênh $k$ trong $x_{l}$ 