"use strict";let _0x135ad9=_0x2010;function _0x2010($,t){let x=_0x1e05();return(_0x2010=function($,t){return x[$-=499]})($,t)}function _0x1e05(){let $=["382002DtIJiV","7147629LMLlim","Error: ","35mqFIvZ","425973dNLsjr","post","1329382GwNtVq","application/json","Please specify a question!","question","5773912YOErOR","1731632nqjNhW","data","https://vihangayt.me/tools/bard","Please specify a URL for the image!","2645305UGDqSm","questionWithImage","6byOWDz","message"];return(_0x1e05=function(){return $})()}!function($,t){let x=_0x2010,e=$();for(;;)try{let a=-parseInt(x(508))/1+-parseInt(x(510))/2+-parseInt(x(502))/3*(-parseInt(x(515))/4)+-parseInt(x(500))/5+-parseInt(x(504))/6*(parseInt(x(507))/7)+parseInt(x(514))/8+parseInt(x(505))/9;if(443676===a)break;e.push(e.shift())}catch(r){e.push(e.shift())}}(_0x1e05,443676);import $ from"axios";class Bard{constructor(){}async [_0x135ad9(513)]({ask:t}){let x=_0x135ad9;if(!t)throw Error(x(512));try{let e=await $.post(x(517),{ask:t},{headers:{"Content-Type":x(511)}});return e.data}catch(a){throw Error(x(506)+a.message)}}async [_0x135ad9(501)]({ask:t,image:x}){let e=_0x135ad9;if(!t)throw Error(e(512));if(!x)throw Error(e(499));try{let a=await $[e(509)]("https://bard.rizzy.eu.org/api/onstage/image",{ask:t,image:x},{headers:{"Content-Type":e(511)}});return a[e(516)]}catch(r){throw Error(e(506)+r[e(503)])}}}export default Bard;