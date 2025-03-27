# Secure File Share Slack App

## Inspiration
The idea came from the need to share files securely by classifying the documents in corporate environments, especially when sensitive documents like Contracts, Invoices or any documents that has PII involved.  I wanted to automate the entire process - From uploading the file to slack notification and ensuring every shared document is processed with intelligence and accountability. 

## What it does
This allows user to upload the document via web app along with information about which slack group that person want to share the file. This info is stored in table storage. Once the file is uploaded, a logic app triggers Azure AI services like **Document Intelligence** and **Computer Vision** to analyze the document and classify it. Finally, a slack notification is sent with the SAS URI of the file to intended recipient or channel.

## How we built it
<ol>
<li>Azure Web App to build the website with Python (Flask) to handle uploads and route the metadata. </li>
<li>Azure Logic App to automate the entire workflow, once the file is uploaded.</li>
<li>Azure Blob Storage to store uploaded files securely. </li>
<li>Azure Table Storage to log metadata like Filename, From_user, To_user or Slack Channel.</li>
<li>Azure Document Intelligence to extract data from documents and classify the document. </li>
<li>Azure AI Vision to extract data from images or screenshots and classify it. </li>
<li>Slack to alert the channel or users in real time. </li>
</ol>

## Challenges we ran into
Initially I intended to do a Teams integration, spent a lot of time trying to configure Teams using app registrations, direct logins etc. but I don't have the necessary licenses to make it work, so I chose a different messaging app. 

## Accomplishments that we're proud of
<ol>
  <li>Fully automated pipeline with no manual intervention.</li>
  <li>A scalable solution using native Azure components with minimal custom code. </li>
  <li>Successfully integrated AI services to extract and classify the documents.</li>
</ol>

## What we learned
<ol>
  <li>Efficient use of Azure Table Storage for lightweight metadata logging instead of spinning up a SQL database.</li>
  <li>Working with Azure AI services - AI Vision and Document Intelligence</li>
  <li>Learned a lot on various connectors inside Azure Logic Apps. </li>
</ol>

## What's next for Secure File Share Slack App
<ol>
  <li>Currently, authentication is not configured. I would like to add authentication to restrict uploads and access only to the Entra or authenticated users.  </li>
  <li>Life cycle management based on the type of document. If it is Highly classified then the access must be restricted to few minutes and also delete the file from Storage account.</li>
  <li>Expand to Outlook and Microsoft Teams integration. </li>
</ol>
