document.addEventListener('DOMContentLoaded', function(){














  // 숫자 3자리 콤마찍기...

Number.prototype.formatNumber = function(){

  if(this==0) return 0;

  let regex = /(^[+-]?\d+)(\d)/;

  let nstr = (this + '');

  while (regex.test(nstr)) nstr = nstr.replace(regex, '$1' + ',' + '$2');

  return nstr;

};