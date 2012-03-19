# -*- encoding: utf-8 -*-

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time

from osv import fields, osv
from tools.translate import _
import decimal_precision as dp
import netsvc

<<<<<<< HEAD
def arrot(cr,uid,valore,decimali):
    #import pdb;pdb.set_trace()
    return round(valore,decimali(cr)[1])

=======
>>>>>>> 9c0b1c1f2bc7436937a85f075c2fd6c3b3d3defd
class FiscalDocRighe(osv.osv):
   _inherit = "fiscaldoc.righe"



   
   _columns = {
                'extra_price_variant':fields.float('Prezzo Extra', digits_compute= dp.get_precision('Sale Price')),
               }
   
   
<<<<<<< HEAD
   def calcola_netto_merce(self, cr, uid, ids, context):
       # toglie dal totale merce gli sconti di testata 
        lines = self.pool.get('fiscaldoc.righe').search(cr, uid, [('name', '=', ids)])      
        tot_merce = 0
        #import pdb;pdb.set_trace()
        for riga in self.pool.get('fiscaldoc.righe').browse(cr, uid, lines, context=context):
            tot_merce= (riga.prezzo_netto+riga.extra_price_variant)*riga.product_uom_qty
            if riga.name.sconto_pagamento:
                tot_merce = tot_merce-(tot_merce*riga.name.sconto_pagamento/100)
            if riga.name.sconto_partner:
                tot_merce= tot_merce-(tot_merce*riga.name.sconto_partner/100)
            #tot_merce = tot_merce + riga['totale_riga']
            ok = self.pool.get('fiscaldoc.righe').write(cr,uid,riga.id,{'totale_riga':tot_merce})
        return True   
   

   def totale_riga(self,cr,uid,qty, netto,extra_price_variant=False):
=======

   def totale_riga(self,qty, netto,extra_price_variant=False):
>>>>>>> 9c0b1c1f2bc7436937a85f075c2fd6c3b3d3defd
       #import pdb;pdb.set_trace()
       if qty and netto:
        if extra_price_variant:
           netto = netto+extra_price_variant
       else:
<<<<<<< HEAD
	          qty=netto = 0.0
       tot = qty * netto      
       tot = arrot(cr,uid,tot,dp.get_precision('Account'))
       return tot
   
   def onchange_articolo(self, cr, uid, ids, product_id, listino_id, qty, partner_id, data_doc, uom,context):
      res =super(FiscalDocRighe,self).onchange_articolo(cr, uid, ids, product_id, listino_id, qty, partner_id, data_doc, uom,context)
=======
	  qty=netto = 0.0

       return qty * netto
   
   def onchange_articolo(self, cr, uid, ids, product_id, listino_id, qty, partner_id, data_doc, uom):
      res =super(FiscalDocRighe,self).onchange_articolo(cr, uid, ids, product_id, listino_id, qty, partner_id, data_doc, uom)
>>>>>>> 9c0b1c1f2bc7436937a85f075c2fd6c3b3d3defd
      #import pdb;pdb.set_trace()
      if res:
       v=res.get('value',{})
       if product_id:            
            product_obj = self.pool.get('product.product')
            riga_art = product_obj.browse(cr, uid, product_id)   
            if riga_art:
                v['extra_price_variant'] = riga_art.price_extra
<<<<<<< HEAD
                v['totale_riga'] = self.totale_riga(cr,uid,qty, v['prezzo_netto'],v['extra_price_variant'])
=======
                v['totale_riga'] = self.totale_riga(qty, v['prezzo_netto'],v['extra_price_variant'])
>>>>>>> 9c0b1c1f2bc7436937a85f075c2fd6c3b3d3defd
       else:
           v={} 
                
      return {'value':v}       

<<<<<<< HEAD
   def on_change_qty(self, cr, uid, ids, product_id, listino_id, qty, partner_id, uom, data_doc,context,extra_price_variant=False):
        res =super(FiscalDocRighe,self).on_change_qty(cr, uid, ids, product_id, listino_id, qty, partner_id, uom, data_doc,context)
=======
   def on_change_qty(self, cr, uid, ids, product_id, listino_id, qty, partner_id, uom, data_doc,extra_price_variant=False):
        res =super(FiscalDocRighe,self).on_change_qty(cr, uid, ids, product_id, listino_id, qty, partner_id, uom, data_doc)
>>>>>>> 9c0b1c1f2bc7436937a85f075c2fd6c3b3d3defd
        #import pdb;pdb.set_trace()
        if res:            
            v = res.get('value',{})  
            if v.get('prezzo_netto',False):
<<<<<<< HEAD
	      v['totale_riga'] = self.totale_riga(cr,uid,qty, v['prezzo_netto'],extra_price_variant) 
=======
	      v['totale_riga'] = self.totale_riga(qty, v['prezzo_netto'],extra_price_variant) 
>>>>>>> 9c0b1c1f2bc7436937a85f075c2fd6c3b3d3defd
        else:
           v={} 
            
        return {'value':v}            

   def on_change_prezzo(self, cr, uid, ids, prezzo, sconto, qty,extra_price_variant=False):
     
       res =super(FiscalDocRighe,self).on_change_prezzo(cr, uid, ids, prezzo, sconto, qty)
       #import pdb;pdb.set_trace()
       if res:
        v = res.get('value',{})
        if v.get('prezzo_netto',False):
<<<<<<< HEAD
            v['totale_riga'] = self.totale_riga(cr,uid,qty, v['prezzo_netto'],extra_price_variant)  
=======
            v['totale_riga'] = self.totale_riga(qty, v['prezzo_netto'],extra_price_variant)  
>>>>>>> 9c0b1c1f2bc7436937a85f075c2fd6c3b3d3defd
       else:
           v={} 
             
       return {'value':v}   
   
   def on_change_strSconti(self, cr, uid, ids, value, prezzo, qty,extra_price_variant=False):
       #import pdb;pdb.set_trace()
      res =super(FiscalDocRighe,self).on_change_strSconti( cr, uid, ids, value, prezzo, qty)
      #import pdb;pdb.set_trace()
      if res:        
        v = res.get('value',{})  
        if v.get('prezzo_netto',False):
<<<<<<< HEAD
            v['totale_riga'] = self.totale_riga(cr,uid,qty, v['prezzo_netto'],extra_price_variant)
=======
            v['totale_riga'] = self.totale_riga(qty, v['prezzo_netto'],extra_price_variant)
>>>>>>> 9c0b1c1f2bc7436937a85f075c2fd6c3b3d3defd
        else:
            sconto = 0
      else:
           v={} 
            

      return  {'value': v}
    
   def onchange_flag(self, cr, uid, ids, product_id, listino_id, qty, partner_id, data_doc, uom, flag_omaggi,extra_price_variant=False):    
       #import pdb;pdb.set_trace()
       res =super(FiscalDocRighe,self).onchange_flag( cr, uid, ids, product_id, listino_id, qty, partner_id, data_doc, uom, flag_omaggi)
       #import pdb;pdb.set_trace()
       if res:
        v = res.get('value',{})  
        if  v['totale_riga']<>0:
<<<<<<< HEAD
            v['totale_riga'] = self.totale_riga(cr,uid,qty, v['prezzo_netto'],extra_price_variant)
=======
            v['totale_riga'] = self.totale_riga(qty, v['prezzo_netto'],extra_price_variant)
>>>>>>> 9c0b1c1f2bc7436937a85f075c2fd6c3b3d3defd
       else:
           v={} 
            
       return  {'value': v}                 

FiscalDocRighe()
