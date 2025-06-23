import streamlit as st
import os
from agents.leadbot import LeadBot
from agents.replygenie import ReplyGenie
from agents.socialagent import SocialAgent
from agents.editorbot import EditorBot
from agents.clientmailer import ClientMailer
from agents.feedbackai import FeedbackAI
from agents.invoicebot import InvoiceBot

st.set_page_config(page_title='QuartzOS Dashboard', layout='wide')
st.title('QuartzOS AI Agent Dashboard')

# Instantiate agents
leadbot = LeadBot()
replygenie = ReplyGenie()
socialagent = SocialAgent()
editorbot = EditorBot()
clientmailer = ClientMailer()
feedbackai = FeedbackAI()
invoicebot = InvoiceBot()

st.sidebar.header('Trigger Agents')

if st.sidebar.button('Run LeadBot'):
    st.write('LeadBot triggered! (placeholder)')
    # leadbot.read_gmail_leads() ...

if st.sidebar.button('Run ReplyGenie'):
    st.write('ReplyGenie triggered! (placeholder)')

if st.sidebar.button('Run SocialAgent'):
    st.write('SocialAgent triggered! (placeholder)')

if st.sidebar.button('Run EditorBot'):
    st.write('EditorBot triggered! (placeholder)')

if st.sidebar.button('Run ClientMailer'):
    st.write('ClientMailer triggered! (placeholder)')

if st.sidebar.button('Run FeedbackAI'):
    st.write('FeedbackAI triggered! (placeholder)')

if st.sidebar.button('Run InvoiceBot'):
    st.write('InvoiceBot triggered! (placeholder)')

st.header('Logs')
st.write('Logs will appear here as agents are triggered.') 