exports.handler = async (event) => {
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers: { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Content-Type' } };
  }
  if (event.httpMethod !== 'POST') return { statusCode: 405, body: 'Method Not Allowed' };

  try {
    const { image, mimeType = 'image/jpeg' } = JSON.parse(event.body ?? '{}');
    if (!image) return { statusCode: 400, body: JSON.stringify({ error: 'Missing image' }) };

    const res = await fetch('https://api.opentyphoon.ai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.TYPHOON_API_KEY}`,
      },
      body: JSON.stringify({
        model: 'typhoon-ocr',
        messages: [{
          role: 'user',
          content: [
            { type: 'image_url', image_url: { url: `data:${mimeType};base64,${image}` } },
            { type: 'text', text: 'อ่านข้อความทั้งหมดในเอกสารนี้ให้ครบถ้วน ส่งคืนเฉพาะข้อความที่อ่านได้เท่านั้น' }
          ]
        }],
        max_tokens: 2048,
      })
    });

    if (!res.ok) {
      const err = await res.text();
      return { statusCode: res.status, headers: { 'Access-Control-Allow-Origin': '*' }, body: JSON.stringify({ error: err }) };
    }

    const data = await res.json();
    const text = data.choices?.[0]?.message?.content ?? '';
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
      body: JSON.stringify({ text })
    };
  } catch (err) {
    return { statusCode: 500, headers: { 'Access-Control-Allow-Origin': '*' }, body: JSON.stringify({ error: String(err) }) };
  }
};
