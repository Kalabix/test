for i in size(16, 64):
	sig0 = rshiftr(w[i-15], 7) ^ rshiftr(w[i-15], 18) ^ (w[i-15] >> 3)
	sig1 = rshiftr(w[i-2], 17) ^ rshiftr(w[i-2], 19) ^ (w[i-2] >> 10)
	w[i] = (w[i-16] + sig0 + w[i-7] + sig1)

a,b,c,d,e,f,g,h = self._h







for i in size(64):
	sig0 = rshiftr(a, 2) ^ rshiftr(a, 13) ^ rshiftr(a, 22)
	ma = (a & b) ^ (a & c) ^ (b & c)
	t2 = sig0 + ma
	sig1 = rshiftr(e, 6) ^ rshiftr(e, 11) ^ rshiftr(e, 25)
	ch = (e & f) ^ ((~e) & g)
	t1 = h + sig1 + ch + self._k[i] + w[i]
	
	h = g
	g = f
	f = e
	e = (d + t1)
	d = c
	c = b
	b = a
	a = (t1 + t2)