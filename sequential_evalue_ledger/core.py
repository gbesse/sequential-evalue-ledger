import math
from .common import number,integer

def run(data):
 events=data['events'];p0=number(data.get('null_probability',.5),1e-9,1-1e-9);alpha=number(data.get('alpha',.05),1e-12,1-1e-12);a=number(data.get('beta_a',1),1e-6,1e6);b=number(data.get('beta_b',1),1e-6,1e6)
 if not isinstance(events,list)or len(events)>10000:raise ValueError('events')
 for x in events:integer(x,0,1)
 logbeta0=math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b);threshold=math.log(1/alpha);successes=0;first=None;maximum=0;rows=[]
 for n,event in enumerate(events,1):
  successes+=event;failures=n-successes;log_e=math.lgamma(a+successes)+math.lgamma(b+failures)-math.lgamma(a+b+n)-logbeta0-successes*math.log(p0)-failures*math.log1p(-p0);maximum=max(maximum,log_e)
  if first is None and log_e>=threshold:first=n
  rows.append({'n':n,'successes':successes,'log_e_value':log_e,'e_value':math.exp(log_e)if log_e<700 else None,'e_value_overflow':log_e>=700,'e_value_underflow':log_e< -745,'crossed_threshold':log_e>=threshold})
 return {'steps':rows,'first_threshold_crossing':first,'maximum_log_e_value':maximum,'log_threshold':threshold,'alpha':alpha,'assumption':'under_null_each_next_binary_event_has_conditional_probability_p0_given_the_past_fixed_prior_and_null','model':'classical_beta_binomial_mixture_likelihood_ratio_e_process_not_repeated_fixed_p_values'}
