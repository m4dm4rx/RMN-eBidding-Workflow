'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const BidSchema = require('../bid_schema.js');

const seedSource = fs.readFileSync(path.join(__dirname, '..', 'seed_bids.js'), 'utf8');
const seedBids = vm.runInNewContext(`${seedSource}\nSEED_BIDS`);
assert.equal(seedBids.length, 649);
for (const row of seedBids) {
  const normalized = BidSchema.normalize(row);
  assert.ok(Object.hasOwn(normalized, 'deliveryDate'));
  assert.ok(Object.hasOwn(normalized, 'warrantyDueDate'));
  assert.ok(Object.hasOwn(normalized, 'retentionReturnStatus'));
}

const existing = {
  _id: 'x1',
  id: '69000000001',
  name: 'เดิม',
  contractPrice: 123456,
  opaqueFutureField: 'keep-me',
  deliveryDate: '2024-05-10',
  warrantyDueDate: '2026-05-10',
  retentionReturnStatus: 'partially_returned',
};

const saved = BidSchema.merge(existing, { name: 'แก้แล้ว' });
assert.equal(saved.name, 'แก้แล้ว');
assert.equal(saved.contractPrice, 123456);
assert.equal(saved.opaqueFutureField, 'keep-me');
assert.equal(saved.deliveryDate, '2024-05-10');
assert.equal(saved.warrantyDueDate, '2026-05-10');
assert.equal(saved.retentionReturnStatus, 'partially_returned');

const created = BidSchema.merge(null, { id: '69000000002' });
assert.equal(created.deliveryDate, null);
assert.equal(created.warrantyDueDate, null);
assert.equal(created.retentionReturnStatus, 'unknown');

const exported = { ...saved };
delete exported._id;
const roundTrip = JSON.parse(JSON.stringify(exported));
assert.equal(roundTrip.deliveryDate, existing.deliveryDate);
assert.equal(roundTrip.warrantyDueDate, existing.warrantyDueDate);
assert.equal(roundTrip.retentionReturnStatus, existing.retentionReturnStatus);
assert.equal(roundTrip.opaqueFutureField, 'keep-me');

const html = fs.readFileSync(path.join(__dirname, '..', 'rmn_ebidding_tracker_2.html'), 'utf8');
assert.ok(html.indexOf('<script src="bid_schema.js"></script>') < html.indexOf('<script src="seed_bids.js"></script>'));
for (const id of ['f-delivery-date', 'f-warranty-due-date', 'f-retention-return-status']) {
  assert.match(html, new RegExp(`id="${id}"`));
}
assert.match(html, /Store\.upsert\(BidSchema\.merge\(existing,/);
assert.match(html, /deliveryDate,warrantyDueDate,retentionReturnStatus/);

// RMN-50: delivered status + guarantee labels
assert.match(html, /DELIVERED:\s*'ส่งงานครบถ้วน'/);
assert.match(html, /<button class="pill" data-filter="delivered">ส่งงานครบถ้วน<\/button>/);
assert.match(html, /<option value="not_returned">ผูกพัน<\/option>/);
assert.match(html, /<option value="returned">รับเงินค้ำประกันคืนแล้ว<\/option>/);
assert.equal(BidSchema.RETURN_STATUSES.has('not_returned') && BidSchema.RETURN_STATUSES.has('returned'), true);

console.log('RMN-36 schema round-trip: PASS');
