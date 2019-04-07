def scanner(products):
    # set the price of the products
    ipd=549.99
    mbp=1399.99
    atv=109.5
    vga=30

    # to count the no. of product that need to be paid
    count_ipd=0
    count_mbp=0
    count_atv=0
    count_vga=0

    # to count the product that is free
    free_atv=0
    free_vga=0

    for i in products:
        if i == 'ipd':
            count_ipd+=1
        elif i=='mbp':
            count_mbp+=1
        elif i=='atv':
            count_atv+=1
        elif i=='vga':
            count_vga+=1
        else:
            continue
    if count_atv/3>=1:
        free_atv=count_atv/(count_atv-count_atv%3)
    if count_ipd>4:
        ipd=499.99

    free_vga=count_mbp

    count_vga-=free_vga
    count_atv-=free_atv

    total_price=ipd*count_ipd+mbp*count_mbp+atv*count_atv+vga*count_vga

    return total_price


sku=[]
print('Please input the product for SKUs scanning, input 0 to stop')
print('SKUs Scanned:')
status=0
while(status==0):
    product=input()
    if product=='0':
        status=1
    sku.append(product)

result=scanner(sku)
print('Total expected: $',result)