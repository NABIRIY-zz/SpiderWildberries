def OriginalPrice(i):
        if i.css('ins.lower-price::text').extract_first() == None:
            return i.css('span.lower-price::text').extract_first()
        else:
            return i.css('ins.lower-price::text').extract_first()

def CurrentPrice(i):
    if i.css('span.price-old-block del::text').extract_first() == None:
        return OriginalPrice(i)
    else:
        return  i.css('span.price-old-block del::text').extract_first()

def Sale(i):
    if CurrentPrice(i) == OriginalPrice(i):
        return "0%"
    else:
        return i.css('span.price-sale.active::text').extract_first()

def Size(i):
    if (i.css('span.sizes').extract_first != None):
        return True
    else:
        return False