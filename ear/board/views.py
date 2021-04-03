from django.shortcuts import render
from django.views import generic
from predict.models import Predict
from user.models import User
from django.utils.decorators import method_decorator
from user.decorators import login_required

@method_decorator(login_required, name = 'dispatch')
class BoardView(generic.ListView):
    model = Predict
    template_name = 'board.html'

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        user = User.objects.get(userid=self.request.session.get('user'))
        context['predict_list'] = Predict.objects.filter(user=user)
        context['username'] = self.request.session.get('user')

        return context 

class BoarddetailView(generic.ListView):
    model = Predict
    template_name = 'board_detail.html'

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

    def get_context_data(self, **kwargs):
        context = super(BoarddetailView, self).get_context_data(**kwargs)
        user = User.objects.get(userid=self.request.session.get('user'))
        context['predict_list'] = Predict.objects.filter(user=user)
        context['username'] = self.request.session.get('user')

        return context 