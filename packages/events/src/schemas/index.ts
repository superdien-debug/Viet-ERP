// ============================================================
// @erp/events - Event Schemas Index
// Re-export all event schemas
// ============================================================

// CRM Schemas
import {
  LeadCreatedSchema,
  LeadScoredSchema,
  LeadConvertedSchema,
  DealWonSchema,
  DealLostSchema,
  CRMEventSchemas,
} from './crm.events';
export {
  LeadCreatedSchema,
  LeadScoredSchema,
  LeadConvertedSchema,
  DealWonSchema,
  DealLostSchema,
  CRMEventSchemas,
};
export type {
  LeadCreated,
  LeadScored,
  LeadConverted,
  DealWon,
  DealLost,
} from './crm.events';

// Accounting Schemas
import {
  InvoiceCreatedSchema,
  InvoiceApprovedSchema,
  InvoicePaidSchema,
  PaymentReceivedSchema,
  JournalEntryPostedSchema,
  AccountingEventSchemas,
} from './accounting.events';
export {
  InvoiceCreatedSchema,
  InvoiceApprovedSchema,
  InvoicePaidSchema,
  PaymentReceivedSchema,
  JournalEntryPostedSchema,
  AccountingEventSchemas,
};
export type {
  InvoiceCreated,
  InvoiceApproved,
  InvoicePaid,
  PaymentReceived,
  JournalEntryPosted,
} from './accounting.events';

// Ecommerce Schemas
import {
  OrderPlacedSchema,
  OrderShippedSchema,
  OrderDeliveredSchema,
  OrderCancelledSchema,
  PaymentCompletedSchema,
  EcommerceEventSchemas,
} from './ecommerce.events';
export {
  OrderPlacedSchema,
  OrderShippedSchema,
  OrderDeliveredSchema,
  OrderCancelledSchema,
  PaymentCompletedSchema,
  EcommerceEventSchemas,
};
export type {
  OrderPlaced,
  OrderShipped,
  OrderDelivered,
  OrderCancelled,
  PaymentCompleted,
} from './ecommerce.events';

// MRP Schemas
import {
  ProductionOrderCreatedSchema,
  ProductionCompletedSchema,
  InventoryUpdatedSchema,
  StockLowSchema,
  QualityCheckPassedSchema,
  MRPEventSchemas,
} from './mrp.events';
export {
  ProductionOrderCreatedSchema,
  ProductionCompletedSchema,
  InventoryUpdatedSchema,
  StockLowSchema,
  QualityCheckPassedSchema,
  MRPEventSchemas,
};
export type {
  ProductionOrderCreated,
  ProductionCompleted,
  InventoryUpdated,
  StockLow,
  QualityCheckPassed,
} from './mrp.events';

// HRM Schemas
import {
  EmployeeOnboardedSchema,
  LeaveRequestedSchema,
  LeaveApprovedSchema,
  PayrollProcessedSchema,
  AttendanceRecordedSchema,
  HRMEventSchemas,
} from './hrm.events';
export {
  EmployeeOnboardedSchema,
  LeaveRequestedSchema,
  LeaveApprovedSchema,
  PayrollProcessedSchema,
  AttendanceRecordedSchema,
  HRMEventSchemas,
};
export type {
  EmployeeOnboarded,
  LeaveRequested,
  LeaveApproved,
  PayrollProcessed,
  AttendanceRecorded,
} from './hrm.events';

/**
 * Unified event schema registry
 * Dùng để lookup schema theo event type
 */
export const AllEventSchemas = {
  ...CRMEventSchemas,
  ...AccountingEventSchemas,
  ...EcommerceEventSchemas,
  ...MRPEventSchemas,
  ...HRMEventSchemas,
} as const;

export type AllEventTypes =
  | keyof typeof CRMEventSchemas
  | keyof typeof AccountingEventSchemas
  | keyof typeof EcommerceEventSchemas
  | keyof typeof MRPEventSchemas
  | keyof typeof HRMEventSchemas;
